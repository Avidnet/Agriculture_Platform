from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views.views import *
from .views import login as log

req_urls = [
    url('login/', log),
    url('refresh/', refresh),
    url('projects/', projects),
]
