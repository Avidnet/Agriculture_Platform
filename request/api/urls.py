from django.urls import path
from .views import *

req_urls = [
    path('login/', login),
    path('projects/', get_projects),
    path('projects/<slug:id>', get_project_detail),
    path('projects/<slug:p_id>/things/', get_project_things),
    path('projects/<slug:p_id>/things/<slug:t_id>', get_thing_detail)

]
