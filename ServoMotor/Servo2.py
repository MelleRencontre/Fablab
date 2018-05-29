# Servo2.py
# Two servo motors driven by PCA9685 chip

from smbus import SMBus
from PCA9685 import PWM
import time

fPWM = 50
i2c_address = 0x40 
channel = 0 
channel2 = 1
channel3 = 2
a = 8.5 
b = 2  

def setup():
    global pwm
    bus = SMBus(1) # Raspberry Pi revision 2
    pwm = PWM(bus, i2c_address)
    pwm.setFreq(fPWM)

def setDirection(direction):
    duty = a / 180 * direction + b
    pwm.setDuty(channel, duty)
    pwm.setDuty(channel2, duty)
    pwm.setDuty(channel3, duty)
    print "direction =", direction, "-> duty =", duty
    time.sleep(1) # allow to settle
   
print "starting"
setup()
##for direction in range(30, 160, 10):
    ##setDirection(direction)
    ##time.sleep(1)
direction = 90
setDirection(direction)    
print "done"
  

