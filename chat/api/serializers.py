from django.conf import settings
from rest_framework import serializers

from UserBase.models import Customer
from chat.models import Conversation, Message, Participant
from chat.utils import TYPE_CUSTOMER, TYPE_SCOUT, ROLE_SENDER, ROLE_RECEIVER
from common.utils import DATETIME_SERIALIZER_FORMAT
from scouts.models import Scout
from utility.logging_utils import sentry_debug_logger
from utility.serializers import DateTimeFieldTZ


class ScoutDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scout
        fields = ('id', 'name', 'profile_pic_url', 'profile_pic_thumbnail_url', 'phone_no')


class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'profile_pic_url', 'profile_pic_thumbnail_url')


class ParticipantSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    class Meta:
        model = Participant
        fields = ('id', 'profile')

    @staticmethod
    def get_profile(obj):
        if obj.type == TYPE_CUSTOMER:
            return CustomerDetailSerializer(Customer.objects.using(settings.HOMES_DB).get(id=obj.customer_id)).data
        elif obj.type == TYPE_SCOUT:
            return ScoutDetailSerializer(obj.scout).data


class MessageSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    created_at = DateTimeFieldTZ(format=DATETIME_SERIALIZER_FORMAT, read_only=True)
    task_id = serializers.SerializerMethodField()
    customer_name = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ('id', 'created_at', 'is_read', 'read_at', 'content', 'role', 'conversation', 'task_id',
                  'customer_name')

    @staticmethod
    def get_task_id(obj):
        try:
            from scouts.api.serializers import ScoutTaskDetailSerializer
            return obj.conversation.task.id
        except Exception as E:
            sentry_debug_logger.error(str(E), exc_info=True)
            return None

    @staticmethod
    def get_customer_name(obj):
        try:
            return obj.conversation.participants.filter(type=TYPE_CUSTOMER).first().name
        except:
            return None

    def get_role(self, obj):
        if obj.sender == self.context['requesting_participant']:
            return ROLE_SENDER
        elif obj.sender == obj.conversation.other_participant(self.context['requesting_participant']):
            return ROLE_RECEIVER

        elif self.context['requesting_participant'].type == TYPE_SCOUT:
            # multiple scout participants possible. All of them sender if not original sender
            return ROLE_SENDER
        else:
            return ROLE_RECEIVER


class ConversationListSerializer(serializers.ModelSerializer):
    other_participant = serializers.SerializerMethodField()
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ('id', 'other_participant', 'task', 'last_message')

    def get_other_participant(self, obj):
        try:
            other_participant = obj.other_participant(self.context['requesting_participant'])
            return ParticipantSerializer(other_participant).data
        except Exception as E:
            from utility.logging_utils import sentry_debug_logger
            sentry_debug_logger.error("error is " + str(E), exc_info=True)
            return None

    def get_last_message(self, obj):
        last_message = obj.last_message
        if last_message:
            return MessageSerializer(last_message, context=self.context).data

