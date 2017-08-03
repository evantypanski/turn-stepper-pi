# turn-stepper-pi
Purpose of this project was to have an Amazon Echo Dot tell a stepper motor to spin through the Raspberry Pi.  This is done with Adafruit IO and a simple on-off switch (thus it may also be controlled from the Adafruit IO dashboard).

The local file to be run is adafruitIOStepper.py.  This is run on the Pi to turn the stepper motor with python.  The files in lambdaFiles are to be run as Amazon lambda code. 

For all libraries used, instead of submodules or simply putting in the git repo, simply install them to the folder yourself.  Use `pip install --target . adafruit-io` to install the required adafruit io library for zipping the directory.

The zip should be saved as "lambdaDeploy.zip" in the lambdaFiles directory in order to be ignored by git ignore.
