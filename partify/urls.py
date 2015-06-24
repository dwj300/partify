"""partify URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', 'frontend.views.index', name='index'),
    url(r'^add_party/$', 'backend.views.add_party', name='add_party'),
    url(r'^party/([0-9]+)/$', 'frontend.views.party', name='party_details'),
    url(r'^add_song/$', 'backend.views.add_song', name='add_song'),
    url(r'^add_vote/([0-9]+)/$', 'backend.views.add_vote', name='add_vote'),
]
