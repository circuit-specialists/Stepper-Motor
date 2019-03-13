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
        self.setSpeed(60)

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
        steps_per_second = (self.speed * self.steps_per_revolution) / 60
        seconds_per_step = 1 / steps_per_second
        # use time base, such as sleep_us = 1000000
        # must use int for ms or us
        us_per_step = int(1000000 * seconds_per_step)
        for step in range(int(steps)):
            self.PULSE.on()
            self.PULSE.off()
            time.sleep_us(us_per_step)

    def test(self):
        time_pulse = 5000
        steps = 200
        for step in range(int(steps)):
            self.PULSE.on()
            self.PULSE.off()
            time.sleep_us(time_pulse)


class DISPLAY:
    def __init__(self):
        print()