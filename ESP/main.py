#!/usr/bin/python
"""
written by Jake Pring from CircuitSpecialists.com
licensed as GPLv3
"""

from machine import Pin
import espressif
import time

class MAIN:
    def __init__(self):
        self.device = espressif.ESP8266()
        self.PULSE = Pin(self.device.D1, Pin.OUT)
        self.DIR = Pin(self.device.D2, Pin.OUT)
        self.setStepsPerRevolution(200) # Out motors are 200 steps per volution
        self.setDirection('CW')
        self.setSpeed(300) # default is 300 RPM for fluid motion

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
        self.speed = float(speed)

    def rotate(self, degrees, direction=None):
        if(direction != None):
            self.setDirection(direction)
        steps = degrees / (360.0 / self.steps_per_revolution)
        self.step(steps)

    def step(self, steps):
        delayTime = 150000.00 / self.speed
        # use time base, such as sleep_us = 1000000
        # must use int for ms or us
        for step in range(int(steps)):
            self.PULSE.on()
            time.sleep_us(20)
            time.sleep_us(delayTime)
            self.PULSE.off()
            time.sleep_us(20)
            time.sleep_us(delayTime)


class DISPLAY:
    def __init__(self):
        print()