#!/usr/bin/python
"""
written by Jake Pring from CircuitSpecialists.com
licensed as GPLv3
"""

from machine import Pin
import time
import network

class STEPPER:
    def __init__(self):
        #self.device = espressif.ESP8266()
        self.PULSE = Pin(17, Pin.OUT)
        self.DIR = Pin(18, Pin.OUT)
        self.setStepsPerRevolution(200.00) # Our motors are 200 steps per revolution
        self.setDirection('CW')
        self.setSpeed(400.00) # default is 600 RPM for fluid motion, Lower will ruin the motor, higher than 1000 will ruin the motor

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
            time.sleep_us(int(delayTime))
            self.PULSE.off()
            time.sleep_us(20)
            time.sleep_us(int(delayTime))

class WiFi:
    def __init__(self, ap_name):
        self.ap = network.WLAN(network.AP_IF)   # create access-point interface
        self.ap.config(essid=ap_name)     # set the ESSID of the access point
        self.ap.active(True)                    # activate the interface


if __name__ == "__main__":
    ## WiFi setup
    wifi = WiFi()

    ## Stepper Control
    motor = STEPPER()