from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import *

urlpatterns = patterns('',
    url(r'^$', index, name='index_view'),
    url(r'^api/power/$', power, name='power_view'),
    url(r'^api/espresso/$', coffee_strong, name='coffee_strong_view'),
    url(r'^api/coffee/$', coffee_normal, name='coffee_normal_view'),
    url(r'^api/strength/(?P<strength>\d+)/$', coffee_strength, name='coffee_strength_view'),
)
