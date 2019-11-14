#!/usr/bin/python
"""
written by Jake Pring from CircuitSpecialists.com
licensed as GPLv3
"""

from machine import Pin
import time


class MOTOR:
    def __init__(self, CP, CW, KP):
        #self.device = espressif.ESP8266()
        self.PULSE = CP
        self.DIR = CW
        self.kill_pin = KP
        # Our motors are 200 steps per revolution
        self.setStepsPerRevolution(200.00)
        self.setDirection('CW')
        # default is 600 RPM for fluid motion, Lower will ruin the motor, higher than 1000 will ruin the motor
        self.setSpeed(400.00)

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
        self.speed = float(speed)

    def rotate(self, degrees, direction=None):
        if(direction != None):
            self.setDirection(direction)
        steps = degrees / (360.00 / self.steps_per_revolution)
        self.step(steps)

    def step(self, steps):
        delayTime = 150000.00 / self.speed
        for step in range(int(steps * 2)):
            self.PULSE.on()
            time.sleep_us(20)
            time.sleep_us(int(delayTime - 20))
            self.PULSE.off()
            time.sleep_us(20)
            time.sleep_us(int(delayTime - 20))
            if(self.kill_pin.value() == 0):
                raise Exception("Emergency Stop Pushed")