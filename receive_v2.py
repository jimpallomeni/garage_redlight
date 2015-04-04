import socket
import RPi.GPIO as GPIO ## Import GPIO library

# Written by John Impallomeni
# April 3, 2015
# Version 1.0
# Red Light recieve


GPIO.cleanup() 

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(16, GPIO.OUT) ## Setup GPIO Pin 16 to OUT as Red
GPIO.setup(18, GPIO.OUT) ## Setup GPIO Pin 18 to OUT as Yellow
GPIO.setup(22, GPIO.OUT) ## Setup GPIO Pin 7 to OUT as Green


# Network Stuff

# socket.setdefaulttimeout(2) #future timeout part

UDP_IP = "192.168.0.205"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
socket.setdefaulttimeout(5)


# Shutdown all ports
GPIO.output(22,False)## Switch Green Off
GPIO.output(18,False)## Switch Yellow Off
GPIO.output(16,False)## Switch Red Off

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    if data == "1":
#	print ("Red Light") # Garage Fully Closed
	GPIO.output(18,False)## Switch Yellow Off
	GPIO.output(22,False)## Switch Green Off
	GPIO.output(16,True)## Red On
	data = 15	
    elif data == "2":
#	print ("Green Light") # Garage Fully Open
	GPIO.output(18,False)## Switch Yellow Off
	GPIO.output(16,False)## Switch Red Off
	GPIO.output(22,True)## Green On
	data = 15
    elif data == "3":
#	print ("Yellow Light") # Garage not fully closed or open
    	GPIO.output(22,False)## Switch Green Off
	GPIO.output(16,False)## Switch Red Off
	GPIO.output(18,True)## Yellow On
	data = 15
    else:
#       print ("Red Light") # Garage Fully Closed
        GPIO.output(18,False)## Switch Yellow Off
        GPIO.output(22,False)## Switch Green Off
        GPIO.output(16,True)## Red On
#       print ("Green Light") # Garage Fully Open
        GPIO.output(18,False)## Switch Yellow Off
        GPIO.output(16,False)## Switch Red Off
        GPIO.output(22,True)## Green On
#       print ("Yellow Light") # Garage not fully closed or open
        GPIO.output(22,False)## Switch Green Off
        GPIO.output(16,False)## Switch Red Off
        GPIO.output(18,True)## Yellow On

