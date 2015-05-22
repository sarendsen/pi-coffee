from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import *

urlpatterns = patterns('',
	url(r'^api/$', on_off_view, name='on_off_view'),
)
