"""realtimenotif URL Configuration

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
from sendnotif.views import home, alert #Added by Suneel Mallela

urlpatterns = patterns([ '',

	#url(r'^$', 'sendnotif.views.home', name='home'),
	#url(r'^alert$', 'sendnotif.views.alert', name='alert'),
	url(r'^$', home, name='home'),                     			#Addedd by SuneelMallela
	url(r'^alert$', alert, name='alert'),		     			#Added by Suneel Mallela
	url(r'^accounts/login/$','django.contrib.auth.views.login',name='login')
    
	#uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)), 
])
