# HomeAutomation-with-AlexaPi
Home Automation using Alexa on Raspberry Pi

Installation Process on Raspberry Pi  
 
Step 1: Setting up Amazon Developer Account  
•	Register and Login to a free Amazon Developer Account from http://developer.amazon.com and go to the Alexa tab.  
•	Go to the Alexa Console -> Products and click on Create Product.  
•	Put in any Product Name and Product ID of choice and select Alexa-Enabled Device in Product type. Also, check all options for end-user interaction.  
•	All other options are irrelevant so click Next to the Security Profiles and click Create New Profile.  
•	Choose any Name and Description and click Next and save Profile ID, Client ID and Client secret.  
•	Add 	‘https://localhost:3000’ 	in 	Allowed 	origins 	and 
‘https://localhost:3000/authresponse’ in Allowed return URLs.  
•	Agree to the terms and click Finish.  
 

Step 2: Clone Alexa into Raspberry Pi  
•	Open a terminal on Raspberry Pi and type cd Desktop and press Enter. Then, Alexa is to be installed on the desktop.  
•	Next, type git clone https://github.com/alexa/alexa-avs-sample-app.git and press Enter, this might take a couple of minutes to download.  
•	Next, enter cd ~/Desktop/alexa-avs-sample-app.  
•	After that enter sudo nano automated_install.sh to edit the installation script. The text editor will open up where the Product ID, Client ID and Client secret that was copied earlier is pasted. Save and Exit  
•	The terminal is back on the screen, enter cd ~/Desktop/alexa-avs-sample-app and .automated_install.sh next to configure and install everything that is needed. This might take as long as 20-25 minutes so wait patiently.  
 
Some questions might need to be answered during the installation when prompted.  
 
 
Step 3: Running Alexa on Raspberry Pi  
•	There are three sets of commands which needs to run simultaneously in three different terminal windows. Do not close any of the terminal windows while running the Alexa  
•	In the first terminal window, the Companion Service of Amazon Web Services is to be started. For that enter cd ~/Desktop/alexa-avs-sample-app/samples and then cd companionService && npm start.  
•	If there is an error that npm is not installed then first npm needs to be installed. In a fresh terminal window type sudo apt-get install npm and press Enter.  
•	Try the above commands again to start the Companion Service. This will open up the port to communicate with Amazon.  
•	Leave that terminal and open a new window and enter cd ~/Desktop/alexa-avssample-app/samples and cd javaclient && mvn exec:exec next.  
•	A Java window will open with a pop up to authenticate the device, click Yes. The browser will open up, another pop-up will appear in the Java app, Do Not click OK yet. Login to the Amazon account in the browser.  
•	Exit the browser once it says ‘device tokens ready’ and then click OK on the Java app pop up. Now the communication with the Amazon servers is active.  
•	Finally, for the last step leave the current terminal window and open a new terminal and enter cd ~/Desktop/alexa-avs-sample-app/samples and cd wakeWordAgent/src && ./wakeWordAgent -e kitt_ai next.  
•	This will start the Wake Word Agent so as to invoke AWS by saying the work ‘Alexa’.  
•	There are two Wake Word Agents available; ‘kitt_ai’ and ‘sensory’. The sensory engine can be started just by replacing ‘kitt_ai’ with ‘sensory’ in the command.  
 
It is suggested to use the sensory engine for wake word as it is more accurate in invoking on ‘Alexa’ utterance. Also, it is less likely go into an idle state after some time of inactivity or after responding to multiple invocations, which is the case with the kitt_ai engine. This is why it is advisable to use sensory engine.  

Open a text editor and copy the following script  
 
#!/bin/bash  
echo "starting companion service"  
cd /home/pi/Desktop/alexa-avs-sample-app/samples/  cd companionService && npm start&  
echo "starting companion service" > alexa_startup.out sleep 5  
echo "starting javaclient"  
cd /home/pi/Desktop/alexa-avs-sample-app/samples/  cd javaclient && mvn exec:exec&  echo "starting javaclient" >> alexa_startup.out  sleep 25  
echo "starting wake word agent"  
cd /home/pi/Desktop/alexa-avs-sample-app/samples/  cd wakeWordAgent/src && ./wakeWordAgent -e kitt_ai&  echo "starting wake word agent" >> alexa_startup.out 
 
 
•	The sleep time may vary from user to user so it is advised to test and make note of the time taken by each step and change the sleep time in the script. The sleep time is very important to make sure the commands never overlap each other’s process.  
•	Change the file path in the script if the installation is in some other location. Save this file as something like ‘alexa_startup.sh’  
•	To run this script, go to the location where this script is saved and open a terminal to that location and enter ‘./alexa_startup.sh’. Wait for the script to run and every other step is the same from there on.  
 
 
 
 
 
Developing Custom Skills  
 
Here below are the steps to create a custom skill to turn on/off LED using GPIO pins with Alexa in raspberry pi.  
•	First up, go to the Amazon Developer Account, next Alexa Consoles -> Skills and click on Create Skill.  
•	Enter a name and click Next, select ‘Custom’ model on the next screen and click Create Skill.  
•	Now, in the Navigation window on the left if the Language is not set to ‘English(IN)’ then go to Language Settings and Add a new language. Remove any other languages to be safe.  
•	The model is now ready to build. Go to Custom -> Invocation and set an invocation name to invoke the skill. For example, ‘Raspberry Pi’.  
•	Go to Intents tab and add a new intent. This intent name should be the same as that of the function that is to be created in Python later. For example, ‘GPIOOnOffIntent’.  
•	Add a new Slot Type, give any name to the slot type like ‘OnOff’ and add two slot values ‘on’ and ‘off’.  
•	Go back to the intent that was created and scroll below to add Intent Slots. Put ‘value’ in Name and select Slot Type that was created in the above steps from the drop-down menu, ‘OnOff’ in this case.  
•	Scroll up again to add Sample Utterance along with Intent Slots in the curly bracket. 
For example, ‘to turn LED {value}’. Make sure to click the ‘+’ to add the utterance.  
•	Click on Save Model and Build Model to build the custom skill. 4.2 Setting up Ngrok  
 
 
•	Ngrok is a program that opens up a secure tunnel behind an HTTPS endpoint. Ngrok makes it possible for Alexa to communicate with the code.  
•	Start up the Raspberry Pi as usual, open up the browser and download the Linux(ARM) version of Ngrok from https://ngrok.com/download.  
•	The download file will be a zip file. Open a terminal and enter unzip /home/pi/ngrokstable-linux-arm.zip  
•	Ngrok is set up now so to run it open up a terminal and enter sudo ./ngrok http 5000  
•	There will be two URLs generated as ngrok is started. In most cases both the addresses would be same but if not make note of the https one.  
•	Go to the skill on the developer console. In the navigation panel, go to Endpoint and enter this address in the default region as ‘https://edfaa975.ngrok.io’ and click save.  
 
 
 
 
 
 
 
 
 
 
 
 
 
Python Programming  
 
•	There are few packages that need to be installed which will be used by the program. Open a terminal and enter  
 
sudo apt-get update && sudo apt-get upgrade -y  sudo apt-get install python2.7-dev python-dev python-pip  sudo pip install Flask flask-ask  
sudo apt-get install rpi.gpio  
 
•	Once the installation is finished everything is set up for the next step. Open any Python IDE, Thorny is installed by default in Raspberry Pi and works perfectly.  
•	Python code to run the Flask server 
 
from flask import Flask from flask_ask import Ask, statement, convert_errors  import RPi.GPIO as GPIO  
import logging  
#importing all the necessary headers  
GPIO.setmode(GPIO.BCM)  
#setting pin mode  app = Flask(__name__)  ask = Ask(app, '/')   
logging.getLogger("flask_ask").setLevel(logging.DEBUG)  
#setting up flask server  
@ask.intent('GPIOOnOffIntent', mapping={'value': 'value'})  def gpio_control(value):  
{  
# function definition  
} 
 
•	Save the program with any name.  
•	This program cannot be run in the IDE as the flask server does not support this. So, open a terminal and start the flask server from here. For example, ‘sudo python gpio_onoff.py’.  
 
This will start the flask server from which the Alexa skill can talk with the python script and call the function.  
Make sure to keep the ngrok and flask server terminals open. The only thing left is to fire up 
Alexa and say “Alexa, ask raspberry pi to turn led on”.  
To control AC loads there is bit complex circuitry involved which will be described in the next chapters. 
 
 
 
 
 
 
 
As mentioned above there are two modes of the Raspberry Pi GPIO pins; Board and BCM.  BCM is more conventionally used with the Raspberry Pi. In the program above pin 18 is set as output pin so the led should be connected across pin 18 and ground. Also, for safety purposes connect a resistor between the LED and the pin as the GPIO pin’s output is 5v which not LEDs can take.  
 
Features like PWM are limited to pin 12, 13 and 18.  
In detail pin diagram is available at https://pinout.xyz/. 
  
GPIO package is not installed by default in Raspberry Pi. So, in the first step, the package was already installed. Now this enables the use of GPIO pins in python programming as well as to manually change the pin status i.e. read/write directly from the terminal.  
 
To write, open a terminal and enter ‘gpio -g write 18 1’, this will make pin 18(BCM) high.  
To read, enter ‘gpio -g read 18’, this will print the status of pin 18, either 1 or 0. 
