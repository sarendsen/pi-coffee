from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import *

urlpatterns = patterns('',
	url(r'^api/power/$', power, name='power_view'),
	url(r'^api/coffee/strong/$', coffee_strong, name='coffee_strong_view'),
	url(r'^api/coffee/normal/$', coffee_normal, name='coffee_normal_view'),
)
