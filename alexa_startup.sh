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
