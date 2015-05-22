from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view, throttle_classes
import RPi.GPIO as GPIO

# 17 = Sterk
# 18 = Normaal
# 27 = Sterkte
# 22 = Aan/Uit

mode = GPIO.getmode()
print mode

HIGH = 1
LOW = 0


@api_view(['GET'])
def on_off_view(request):
    if 'status' not in request.GET:
        return Response()

    requested_status = request.GET['status']

    if requested_status == 'on':
        GPIO.output(18, HIGH)
    elif requested_status == 'off':
        GPIO.output(18, LOW)

    '''
    if GPIO.input(channel):
        print('Input was HIGH')
    else:
        print('Input was LOW')
    '''

    return Response({"message": "sup"})
