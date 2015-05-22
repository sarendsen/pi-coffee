from django.shortcuts import render_to_response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view, throttle_classes
import RPi.GPIO as GPIO
import time

from .models import Setting


# physical pin: 11 / BCM 17 / Aan/Uit
# physical pin: 12 / BCM 18 / Sterkte
# physical pin: 15 / BCM 22 / Normaal
# physical pin: 16 / BCM 23 / Sterk


GPIO.setmode(GPIO.BCM)

mode = GPIO.getmode()

HIGH = 1
LOW = 0

POWER = 17
STRENGTH = 18
NORMAL = 22
STRONG = 23

GPIO.setup([POWER, STRENGTH, NORMAL, STRONG], GPIO.OUT)


def get_setting(key, default=None):
    try:
        obj = Setting.objects.get(key=key)
    except:
        obj = Setting(key='strength', value=default)
        obj.save()

    return obj.value


def save_setting(key, value):
    obj, created = Setting.objects.update_or_create(key=key, value=value)
    return obj


def press(PIN):
    GPIO.output(PIN, HIGH)
    time.sleep(0.4)
    GPIO.output(PIN, LOW)
    time.sleep(0.4)
    GPIO.output(PIN, HIGH)


def index(request):
    return render_to_response('index.html', locals())


@api_view(['GET'])
def power(request):
    if request.GET.get('state', None):
        new_state = str(request.GET.get('state', '1'))
        current_state = str(get_setting('power', '0'))
        #print new_state, current_state
        if new_state != current_state:
            press(POWER)
            print get_setting('power', '0')
            save_setting('power', new_state)
            print get_setting('power', '0')

    return Response({"message": get_setting('power', '0')})

def get_strength_presses(current_strength, new_strength):
    # new : current
    steps = {
        1: {1: 0, 2: 1, 3: 1},
        2: {1: 1, 2: 0, 3: 2},
        3: {1: 2, 2: 1, 3: 0}
    }

    return steps[current_strength][new_strength]


@api_view(['GET'])
def coffee_strength(request, strength):
    strength = int(strength)
    current_strength = get_setting('strength', 3)
    num_presses = get_strength_presses(current_strength, strength)

    for i in xrange(num_presses - 1):
        press(STRENGTH)

    save_setting('strength', strength)

    return Response({"message": "success"})


@api_view(['GET'])
def coffee_strong(request):
    press(STRONG)
    return Response({"message": "success"})


@api_view(['GET'])
def coffee_normal(request):
    press(NORMAL)
    return Response({"message": "success"})
