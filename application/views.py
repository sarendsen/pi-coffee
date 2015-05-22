from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view, throttle_classes
import RPi.GPIO as GPIO
import time


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


def press(PIN):
    GPIO.output(PIN, HIGH)
    time.sleep(0.4)
    GPIO.output(PIN, LOW)
    time.sleep(0.4)
    GPIO.output(PIN, HIGH)


@api_view(['GET'])
def power(request):
    press(POWER)
    return Response({"message": "success"})


@api_view(['GET'])
def coffee_strong(request):
    press(STRONG)
    return Response({"message": "success"})


@api_view(['GET'])
def coffee_normal(request):
    press(NORMAL)
    return Response({"message": "success"})
