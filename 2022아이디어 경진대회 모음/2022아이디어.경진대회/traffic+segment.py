import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(22, GPIO.OUT)#red
GPIO.setup(5, GPIO.OUT)#yellow
GPIO.setup(6, GPIO.OUT)#green

GPIO.setup(27, GPIO.OUT)#a
GPIO.setup(17, GPIO.OUT)#b
GPIO.setup(19,GPIO.OUT)#g
GPIO.setup(23, GPIO.OUT)#c
GPIO.setup(20, GPIO.OUT)#d
GPIO.setup(21, GPIO.OUT)#e
GPIO.setup(13,GPIO.OUT)#f
GPIO.setup(23,GPIO.OUT)#dp


try:
    GPIO.output(22, 0)
    GPIO.output(5, 0)
    GPIO.output(6, 0)
    
    GPIO.output(27, 0)#a
    GPIO.output(17, 0)#b
    GPIO.output(19, 0)#g
    GPIO.output(23, 0)#c
    GPIO.output(20, 0)#d
    GPIO.output(21, 0)#e
    GPIO.output(13, 0)#f
    GPIO.output(23, 0)#dp
    while(True):
        GPIO.output(22, 1)
        time.sleep(5)
        GPIO.output(22, 0)
        GPIO.output(5, 1)
        time.sleep(5)
        GPIO.output(5, 0)
        GPIO.output(6, 1)
        time.sleep(5)

        #5
        GPIO.output(27, 1)#a
        GPIO.output(13, 1)#f
        GPIO.output(19, 1)#g
        GPIO.output(23, 1)#c
        GPIO.output(20, 1)#d
        time.sleep(1)
        GPIO.output(27, 0)#a
        GPIO.output(13, 0)#f
        GPIO.output(19, 0)#g
        GPIO.output(23, 0)#c
        GPIO.output(20, 0)#d

        #4
        GPIO.output(13, 1)#f
        GPIO.output(19, 1)#g
        GPIO.output(17, 1)#b
        GPIO.output(23, 1)#c
        time.sleep(1)
        GPIO.output(13, 0)#f
        GPIO.output(19, 0)#g
        GPIO.output(17, 0)#b
        GPIO.output(23, 0)#c

        #3
        GPIO.output(27, 1)#a
        GPIO.output(17, 1)#b
        GPIO.output(19, 1)#g
        GPIO.output(23, 1)#c
        GPIO.output(20, 1)#d
        time.sleep(1)
        GPIO.output(27, 0)#a
        GPIO.output(17, 0)#b
        GPIO.output(19, 0)#g
        GPIO.output(23, 0)#c
        GPIO.output(20, 0)#d

        #2
        GPIO.output(27, 1)#a
        GPIO.output(17, 1)#b
        GPIO.output(19, 1)#g
        GPIO.output(20, 1)#d
        GPIO.output(21, 1)#e
        time.sleep(1)
        GPIO.output(27, 0)#a
        GPIO.output(17, 0)#b
        GPIO.output(19, 0)#g
        GPIO.output(20, 0)#d
        GPIO.output(21, 0)#e

        #2
        GPIO.output(13, 1)#f
        GPIO.output(21, 1)#e
        time.sleep(1)
        GPIO.output(13, 0)#f
        GPIO.output(21, 0)#e

        
        GPIO.output(6, 0)

        
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Interrupt!! Quit!!")
