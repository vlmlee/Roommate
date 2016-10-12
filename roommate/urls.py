##################################################################################
# This is the root URL routing file in django, 'Roommate/roommate/urls.py'.      #
# Whenever you type something into the address bar, this is the file that        #
# tells django how to serve the client.                                          #
# Below is the default instructions given by django when it generates a project. #
##################################################################################

"""Roommate URL Configuration

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
	# This is an automatically generated entry to allow a user to access the admin console.
    url(r'^admin/', include(admin.site.urls)),

    # This basically creates a mapping to the 'Roommate/match/urls.py file. It is *different* from this file
    # and is often used to namespace different functionality on a web application. The "r'^'" is a regular
    # expression, r standing for "raw", that is special characters are treated as text/unicode. "include" is
    # a method that does some magic to get to the 'Roommate/match/urls.py file.
    url(r'^', include('match.urls')),
]
