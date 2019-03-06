#!/usr/bin/python
"""
written by Jake Pring from CircuitSpecialists.com
licensed as GPLv3
"""

from machine import Pin
import nodeMCU
#import Adafruit_Python_SSD1306
import time

class MAIN:
    def __init__(self):
        self.device = nodeMCU.ESP8266()
        self.PULSE = Pin(self.device.D1, Pin.OUT)
        self.DIR = Pin(self.device.D2, Pin.OUT)
        self.setStepsPerRevolution(200)
        self.setDirection('CW')
        self.setSpeed(1)

    def setStepsPerRevolution(self, steps):
        self.steps_per_revolution = steps

    def setDirection(self, direction):
        if(direction == 'CW'):
            self.DIR.on()
        elif(direction == 'CCW'):
            self.DIR.off()
        else:
            return 'not a valid direction'

    def setSpeed(self, speed):
        # speed = RPM
        self.speed = speed

    def rotate(self, degrees):
        steps = degrees / (360 / self.steps_per_revolution)
        self.cycle(steps)

    def cycle(self, steps):
        time_pulse = self.speed / self.steps_per_revolution / 2
        print(time_pulse)
        for step in range(int(steps)):
            self.PULSE.on()
            time.sleep(time_pulse)
            self.PULSE.off()
            time.sleep(time_pulse)


class DISPLAY:
    def __init__(self):
        print()