from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

)


import RPi.GPIO as GPIO


mode = GPIO.getmode()
print "yo"
print mode
