from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views.views import *
req_urls = [
    url('login/', login),
    url('refresh/', refresh),
    url('projects/', projects),
]