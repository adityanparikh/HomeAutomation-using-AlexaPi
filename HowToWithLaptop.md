If you do not have a Screen or a Mouse or a Keyboard, you can use the Raspberry Pi with your Laptop just using an Ethernet(RJ45) cable and some free to download softwares.
List of Software used:
- PuTTY  
It creates a Secured Shell (SSH) tunnel with the Raspberry Pi’s terminal which can be accessed using its local IP address. SSH is by default disabled in all ‘Raspbian’ versions after ‘Jessie’. To activate SSH an empty file named ‘SSH’ needs to be saved in the boot partition of the SD card. It can also connect to a serial port. 

Default login credentials:

	Username: pi
	Password: raspberry

- VNC Viewer  
A software that provides remote access to the pi using an ethernet cable. It acts as an emulator for the Raspberry Pi with the access to keyboard and mouse too along with the screen to access the Pi. The Pi can be accessed by entering the local IP address into VNC viewer. VNC Viewer comes installed by default in newer versions Raspbian but in older versions, it needs to be installed. PuTTY can be used to install VNC Viewer on the Pi. 

- Advanced IP Scanner  
Advanced IP Scanner is used to find the local IP address of the Raspberry Pi which is used for both PuTTY and VNC Viewer.

- Win32 Disc Imager  
Use an SD card reader to load the Operating System from the computer. But before loading the OS it is always safer to format the SD card (Make sure to format the SD card into FAT32 format). Next step is to load up the OS into the card using any disk imager software for example ‘Win32 Disk Imager’.
  
    
      
The OS can be downloaded from https://www.raspberrypi.org/downloads where two options can be found; ‘Noobs’ and ‘Raspbian’. The user can download the OS of his choice and needs. Then browse the path of the OS into the Disk Imager and Write it on the SD card.

Unfortunately, for installing the OS onto the SD Card for the first-time usage none of the emulators can be used. 
So, connect a screen (any LCD or LED screen) using HDMI and the mouse and keyboard need to be connected via USB ports on the Raspberry Pi. 
Next, Follow the on-screen instructions to install the OS onto the SD card. 
Once the installation commences the Raspberry Pi is completely set up and ready to use.
Or Buy an SD Card pre-installed with Raspbian which is also available in the market.
