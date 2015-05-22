from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view, throttle_classes
import RPi.GPIO as GPIO


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

GPIO.setup([17], GPIO.OUT)


@api_view(['GET'])
def on_off_view(request):
    if 'status' not in request.GET:
        return Response()

    requested_status = request.GET['status']

    if requested_status == 'on':
        GPIO.output(POWER, HIGH)
    elif requested_status == 'off':
        GPIO.output(POWER, LOW)

    '''
    if GPIO.input(channel):
        print('Input was HIGH')
    else:
        print('Input was LOW')
    '''

    return Response({"message": "sup"})
