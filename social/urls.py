"""social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/auth/', include('authapi.urls')),
    url(r'^api/newsfeed/', include('newsfeed.urls')),
    url(r'^api/group/', include('group.urls')),
    url(r'^api/notification/', include('notification.urls')),
    url(r'^api/user/', include('User.urls')),
    url(r'^api/search/', include('search.urls')),
    url(r'^api/event/', include('event.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
