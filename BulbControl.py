import time
from flask import Flask
from flask_ask import Ask, statement, convert_errors
import RPi.GPIO as GPIO
import logging
import random

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18,5000)

app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.intent('GPIOPWMIntent', mapping={'value': 'value'})

def gpio_pwm(value):


    value = int(value)
    
    if value in [0,10,20,30,40,50,60,70,80,90,100]: pwm.start(value)
    else: return statement ('Value not valid')

        
    return statement ('Setting Intensity to {} percent.'.format(value))

@ask.intent('GPIOOnOffIntent', mapping={'status': 'status'})

def gpio_onoff(status):
 
    GPIO.setup(18, GPIO.OUT)

    if status in ['on', 'high']: GPIO.output(18, GPIO.HIGH)
    if status in ['off', 'low']: GPIO.output(18, GPIO.LOW)
    
    return statement('As you wish, Turning bulb {}.'.format(status))

if __name__ == '__main__':
    port = 5000

app.run(host='0.0.0.0', port=port)
    