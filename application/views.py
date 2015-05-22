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


#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)

mode = GPIO.getmode()

HIGH = 1
LOW = 0

POWER = 17
STRENGTH = 18
NORMAL = 22
STRONG = 23

GPIO.setup([POWER, STRENGTH, NORMAL, STRONG], GPIO.OUT)


@api_view(['GET'])
def power_view(request):
    if 'status' not in request.GET:
        return Response()

    requested_status = request.GET['status']

    if requested_status in ['on', 'off']:
        GPIO.output(POWER, HIGH)
        time.sleep(0.5)
        GPIO.output(POWER, LOW)
        time.sleep(0.5)
        GPIO.output(POWER, HIGH)

    GPIO.cleanup()
    return Response({"message": "success"})
