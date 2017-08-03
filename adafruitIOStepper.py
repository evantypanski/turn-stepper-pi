import time
from Adafruit_IO import *
import RPi.GPIO as GPIO

pin = 2                 # Our LED is on GPIO pin 2
direction = 4
step = 3

with open('key.txt') as f:
	key = f.readline()  # Load key from separate file - first line of key.txt
key = key.strip('\n')       # Remove newline character from key

while True:
    client = Client(key)

    if int(client.receive('OnOff').value):
        client.send('OnOff', 0)

        # Light up LED
        GPIO.setmode(GPIO.BCM)  # BCM for GPIO numbering
        GPIO.setwarnings(False) # Disable warnings

        GPIO.setup(pin, GPIO.OUT)
        for x in range(0,1):
            GPIO.output(pin, True)
            time.sleep(1)
            GPIO.output(pin, False)
            time.sleep(1)

        # Setup
        GPIO.setup(direction, GPIO.OUT)
        GPIO.setup(step, GPIO.OUT)

	GPIO.output(direction, True)
	for x in range(0, 1000):
	    # Turn Stepper Motor
	    GPIO.output(step, False)
	    time.sleep(0.0001)
	    GPIO.output(step, True)
	    time.sleep(0.0001)

	GPIO.output(direction, False)
	for x in range(0, 500):
	    # Turn Stepper Motor
	    GPIO.output(step, False)
	    time.sleep(0.0001)
	    GPIO.output(step, True)
	    time.sleep(0.0001)

        # Cleanup
        GPIO.cleanup()

    time.sleep(1)
