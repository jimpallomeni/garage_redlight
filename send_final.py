import time
import RPi.GPIO as GPIO
import socket
import smtplib
import subprocess

# Written by John Impallomeni
# April 3, 2015
# Version 1.0

# Setup a crontab @reboot running as root
# All files should be copied to "/usr/tfd/"

# Magnetic switch pins
# Garage open pin = 25
# Garage closed pin = 23

#Redlight Pi - Replace with your own info
UDP_IP = "192.168.0.205"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

#Light Status
OPEN = "2"
CLOSED = "1"
YELLOW = "3" 

#Set alert to yellow
ALERT = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
	if(GPIO.input(23) == 0 and ALERT == 1):
                sock.sendto(CLOSED, (UDP_IP, UDP_PORT))
		subprocess.call(['/usr/tfd/closed.sh'])
		ALERT = 0
                time.sleep(1)
        elif(GPIO.input(25) == 0 and ALERT == 1):
                sock.sendto(OPEN, (UDP_IP, UDP_PORT))
		subprocess.call(['/usr/tfd/open.sh'])
		ALERT = 0
		time.sleep(1)
	elif(GPIO.input(23) == 0):
		sock.sendto(CLOSED, (UDP_IP, UDP_PORT))
		ALERT = 0
		time.sleep(1)	
	elif(GPIO.input(25) == 0):
        	sock.sendto(OPEN, (UDP_IP, UDP_PORT))
		ALERT = 0
		time.sleep(1)
    	else:
	        sock.sendto(YELLOW, (UDP_IP, UDP_PORT))
		ALERT = 1	
		time.sleep(.5)
GPIO.cleanup()
time.sleep(1)

