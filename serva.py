import serial
import threading
import sys
import time
import RPi.GPIO as GPIO
import socket
socket = socket.socket()
socket.bind(('', 15555))




def serv(a, b, c, d, ryzen):
        GPIO.setmode(GPIO.BCM)
 
        # Define GPIO signals to use
        # Physical pins 11,15,16,18
        # GPIO17,GPIO22,GPIO23,GPIO24
        StepPins = [a,b,c,d]
         
        # Set all pins as output
        for pin in StepPins:
                print "Setup pins"
                GPIO.setup(pin,GPIO.OUT)

        # Define advanced sequence
        # as shown in manufacturers datasheet
        Seq = [[1,0,0,1],
               [1,0,0,0],
               [1,1,0,0],
               [0,1,0,0],
               [0,1,1,0],
               [0,0,1,0],
               [0,0,1,1],
               [0,0,0,1]]
                
        StepCount = len(Seq)
        StepDir = 1 # Set to 1 or 2 for clockwise
                    # Set to -1 or -2 for anti-clockwise
         
        # Read wait time from command line
        if len(sys.argv)>1:
                WaitTime = int(sys.argv[1])/float(1000)
        else:
                WaitTime = 1/float(1000)
         
        # Initialise variables
        StepCounter = 0
	while True:
                debianeuf = client.recv(255)
                if debianeuf == "a":
                        StepDir  = -1
                        v = True
                elif debianeuf == "b":
                        StepDir = 1
                        v = True
                elif debianeuf == "c":
                        if ryzen == "intel":
                                StepDir = -1
                        elif ryzen == "amd":
                                StepDir = 1
                        v = True
                elif debianeuf == "d":
                        if ryzen == "intel":
                                StepDir = 1
                        elif ryzen == "amd":
                                StepDir = -1
                        v = True
                else:
                        v = False
                
                a = 0
                if v == True:
                        while a < 500:
                                print a
                                a = a+1
                                print StepCounter,
                                print Seq[StepCounter]
                                 
                                for pin in range(0, 4):
                                        xpin = StepPins[pin]
                                        if Seq[StepCounter][pin]!=0:
                                                print " Enable GPIO %i" %(xpin)
                                                GPIO.output(xpin, True)
                                        else:
                                                GPIO.output(xpin, False)
                                 
                                StepCounter += StepDir
                                 
                                  # If we reach the end of the sequence
                                  # start again
                                if (StepCounter>=StepCount):
                                        StepCounter = 0
                                if (StepCounter<0):
                                        StepCounter = StepCount+StepDir
                                time.sleep(0.001)
                                 
                                  # Wait before moving on

                                

	client.close()
	stock.close()

while 1:
	socket.listen(5)
	client, address = socket.accept()
	print("{} connected".format( address ))
	threading.Thread(target=serv, args=(17, 22, 23, 24, "intel")).start()
	threading.Thread(target=serv, args=(6, 13, 19, 26, "amd")).start()
