#### Step 1: Setting up Amazon Developer Account

- Register and Login to a free Amazon Developer Account from http://developer.amazon.com and go to the Alexa tab.
- Go to the Alexa Console -> Products and click on Create Product.
- Put in any Product Name and Product ID of choice and select Alexa-Enabled Device in Product type. Also, check all options for end-user interaction.
- All other options are irrelevant so click Next to the Security Profiles and click Create New Profile.
- Choose any Name and Description and click Next and save Profile ID, Client ID and Client secret.
- Add ```https://localhost:3000```  in Allowed origins and ```https://localhost:3000/authresponse``` in Allowed return URLs.
- Agree to the terms and click Finish.

#### Step 2: Clone Alexa into Raspberry Pi

- Open a terminal on Raspberry Pi and type cd Desktop and press Enter. Then, Alexa is to be installed on the desktop.
- Next, type ```git clone https://github.com/alexa/alexa-avs-sample-app.git``` and press Enter, this might take a couple of minutes to download.
- Next, enter ```cd ~/Desktop/alexa-avs-sample-app```.
- After that enter _sudo nano automated_install.sh_ to edit the installation script. The text editor will open up where the Product ID, Client ID and Client secret that was copied earlier is pasted. Save and Exit
- The terminal is back on the screen, enter ```cd ~/Desktop/alexa-avs-sample-app``` and .automated_install.sh next to configure and install everything that is needed. This might take as long as 20-25 minutes so wait patiently. 


Some questions might need to be answered during the installation when prompted.


#### Step 3: Running Alexa on Raspberry Pi

There are three sets of commands which needs to run simultaneously in three different terminal windows. Do not close any of the terminal windows while running the Alexa

- In the first terminal window, the Companion Service of Amazon Web Services is to be started. For that enter ```cd ~/Desktop/alexa-avs-sample-app/samples and then cd companionService && npm start```.
- If there is an error that npm is not installed then first npm needs to be installed. In a fresh terminal window type ```sudo apt-get install npm``` and press Enter.
- Try the above commands again to start the Companion Service. This will open up the port to communicate with Amazon.
- Leave that terminal and open a new window and enter ```cd ~/Desktop/alexa-avs-sample-app/samples and cd javaclient && mvn exec:exec next```.
- A Java window will open with a pop up to authenticate the device, click Yes. The browser will open up, another pop-up will appear in the Java app, Do Not click OK yet. Login to the Amazon account in the browser. 
- Exit the browser once it says ‘device tokens ready’ and then click OK on the Java app pop up. Now the communication with the Amazon servers is active.
- Finally, for the last step leave the current terminal window and open a new terminal and enter ```cd ~/Desktop/alexa-avs-sample-app/samples and cd wakeWordAgent/src && ./wakeWordAgent -e kitt_ai next```.
- This will start the Wake Word Agent so as to invoke AWS by saying the work ‘Alexa’.
- There are two Wake Word Agents available; ‘kitt_ai’ and ‘sensory’. The sensory engine can be started just by replacing ‘kitt_ai’ with ‘sensory’ in the command.


It is suggested to use the sensory engine for wake word as it is more accurate in invoking on ‘Alexa’ utterance. Also, it is less likely go into an idle state after some time of inactivity or after responding to multiple invocations, which is the case with the kitt_ai engine. This is why it is advisable to use sensory engine.





Open a text editor and copy the following script
```
#!/bin/bash

echo "starting companion service"
cd /home/pi/Desktop/alexa-avs-sample-app/samples/
cd companionService && npm start&
echo "starting companion service" > alexa_startup.out

sleep 5

echo "starting javaclient"
cd /home/pi/Desktop/alexa-avs-sample-app/samples/
cd javaclient && mvn exec:exec&
echo "starting javaclient" >> alexa_startup.out

sleep 25

echo "starting wake word agent"
cd /home/pi/Desktop/alexa-avs-sample-app/samples/
cd wakeWordAgent/src && ./wakeWordAgent -e kitt_ai&
echo "starting wake word agent" >> alexa_startup.out
```
- The sleep time may vary from user to user so it is advised to test and make note of the time taken by each step and change the sleep time in the script. The sleep time is very important to make sure the commands never overlap each other’s process.
- Change the file path in the script if the installation is in some other location. Save this file as something like ‘alexa_startup.sh’
- To run this script, go to the location where this script is saved and open a terminal to that location and enter ‘./alexa_startup.sh’. Wait for the script to run and every other step is the same from there on.
