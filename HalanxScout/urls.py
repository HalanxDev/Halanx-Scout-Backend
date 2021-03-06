from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from scouts.api.views import ChangePasswordView
from utility.environments import DEVELOPMENT

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^rest-auth/password/change/$', ChangePasswordView.as_view()),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^accounts/', include('allauth.urls')),

    url(r'^scouts/', include('scouts.urls')),

    url(r'^chat/', include('chat.urls')),
    url(r'^chat/realtime/', include('chat.urls')),

]


if settings.DEBUG and settings.ENVIRONMENT == DEVELOPMENT:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
