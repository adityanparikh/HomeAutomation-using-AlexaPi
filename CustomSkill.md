## How to build an Alexa Custom Skill
Here below are the steps to create a custom skill to turn on/off LED using GPIO pins with Alexa in raspberry pi.

- First up, go to the Amazon Developer Account, next Alexa Consoles -> Skills and click on Create Skill.
- Enter a name and click Next, select ‘Custom’ model on the next screen and click Create Skill.
- Now, in the Navigation window on the left if the Language is not set to ‘English(IN)’ then go to Language Settings and Add a new language. Remove any other languages to be safe.
- The model is now ready to build. Go to Custom -> Invocation and set an invocation name to invoke the skill. For example, ‘Raspberry Pi’.
- Go to Intents tab and add a new intent. This intent name should be the same as that of the function that is to be created in Python later. For example, ‘GPIOOnOffIntent’.
- Add a new Slot Type, give any name to the slot type like ‘OnOff’ and add two slot values ‘on’ and ‘off’.
- Go back to the intent that was created and scroll below to add Intent Slots. Put ‘value’ in Name and select Slot Type that was created in the above steps from the drop-down menu, ‘OnOff’ in this case.
- Scroll up again to add Sample Utterance along with Intent Slots in the curly bracket. For example, ‘to turn LED {value}’. Make sure to click the ‘+’ to add the utterance.
- Click on Save Model and Build Model to build the custom skill.

#### Setting up Ngrok   
Ngrok is a program that opens up a secure tunnel behind an HTTPS endpoint. Ngrok makes it possible for Alexa to communicate with the code.

- Start up the Raspberry Pi as usual, open up the browser and download the Linux(ARM) version of Ngrok from ```https://ngrok.com/download```.
- The download file will be a zip file. Open a terminal and enter unzip ```/home/pi/ngrok-stable-linux-arm.zip```
- Ngrok is set up now so to run it open up a terminal and enter ```sudo ./ngrok http 5000```
- There will be two URLs generated as ngrok is started. In most cases both the addresses would be same but if not make note of the https one.
- Go to the skill on the developer console. In the navigation panel, go to Endpoint and enter this address in the default region as ```https://edfaa975.ngrok.io``` and click save.

#### Python Programming  
- There are few packages that need to be installed which will be used by the program. Open a terminal and enter 
```
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install python2.7-dev python-dev python-pip
sudo pip install Flask flask-ask
sudo apt-get install rpi.gpio
```

- Once the installation is finished everything is set up for the next step. Open any Python IDE, Thorny is installed by default in Raspberry Pi and works perfectly.
- The program to turn on/off is as below:
```
from flask import Flask
from flask_ask import Ask, statement, convert_errors
import RPi.GPIO as GPIO
import logging

#importing all the necessary headers

GPIO.setmode(GPIO.BCM)

#setting pin mode
app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

#setting up flask server

@ask.intent('GPIOOnOffIntent', mapping={'value': 'value'})
def gpio_control(value):

{
# function definition 
} 
```

Sample LED On/Off program can be [GPIO_OnOff](gpio_onoff.py).
- Save the program with any name. 
- This program cannot be run in the IDE as the flask server does not support this. So, open a terminal and start the flask server from here. For example, ‘sudo python gpio_onoff.py’.

This will start the flask server from which the Alexa skill can talk with the python script and call the function.

Make sure to keep the ngrok and flask server terminals open. The only thing left is to fire up Alexa and say “Alexa, ask raspberry pi to turn led on”. 

As mentioned above there are two modes of the Raspberry Pi GPIO pins; Board and BCM. 

BCM is more conventionally used with the Raspberry Pi. In the program above pin 18 is set as output pin so the led should be connected across pin 18 and ground. Also, for safety purposes connect a resistor between the LED and the pin as the GPIO pin’s output is 5v which not LEDs can take.

Features like PWM are limited to pin 12, 13 and 18.
In detail pin diagram is available at ```https://pinout.xyz/```.

GPIO package is not installed by default in Raspberry Pi. So, in the first step, the package was already installed. Now this enables the use of GPIO pins in python programming as well as to manually change the pin status i.e. read/write directly from the terminal.

To write, open a terminal and enter ‘gpio -g write 18 1’, this will make pin 18(BCM) high.
To read, enter ‘gpio -g read 18’, this will print the status of pin 18, either 1 or 0.
