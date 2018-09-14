from flask import Flask
from flask_ask import Ask, statement, convert_errors
import RPi.GPIO as GPIO
import logging
import random

GPIO.setmode(GPIO.BCM)

app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.intent('GPIOOnOffIntent', mapping={'status': 'status'})
def gpio_onoff(status):
 
    GPIO.setup(18, GPIO.OUT)

    if status in ['on', 'high']: GPIO.output(18, GPIO.HIGH)
    if status in ['off', 'low']: GPIO.output(18, GPIO.LOW)
    
    return statement('OK, Turning bulb {}.'.format(status))
 
if __name__ == '__main__':
    port = 5000

app.run(host='0.0.0.0', port=port)
