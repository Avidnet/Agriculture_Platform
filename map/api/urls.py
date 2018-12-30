from django.conf.urls import url
from django.views.generic import TemplateView


map_url = [
    url('cal', TemplateView.as_view(template_name='calendar.html'), name='cal'),
    url('w', TemplateView.as_view(template_name='weather.html'), name='w'),

    url('', TemplateView.as_view(template_name='index.html'), name='index'),

]
