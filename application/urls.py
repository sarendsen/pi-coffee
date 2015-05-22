from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import *

urlpatterns = patterns('',
	url(r'^api/power/$', power_view, name='power_view'),
)
