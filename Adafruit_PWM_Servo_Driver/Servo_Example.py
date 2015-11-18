#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)

servoMin = 1000  # Min pulse length out of 4096
servoMax = 4000  # Max pulse length out of 4096

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(1000)                        # Set frequency to 60 Hz
while (True):
  # Change speed of continuous servo on channel O
#  for i in range(8):
#    pwm.setPWM(i, 0, servoMin)
#  time.sleep(2);
  for i in range(8):
    pwm.setPWM(i, 1000, 4095)
  time.sleep(1)
  for i in range(8):
    pwm.setPWM(i, 1000, 2000)
  time.sleep(1)

