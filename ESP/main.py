#!/usr/bin/python
"""
written by Jake Pring from CircuitSpecialists.com
licensed as GPLv3
"""

from machine import Pin
import time
import network
import stepper

class WiFi:
    def __init__(self, ap_name):
        self.ap = network.WLAN(network.AP_IF)   # create access-point interface
        self.ap.config(essid=ap_name)           # set the ESSID of the access point
        self.ap.active(True)                    # activate the interface


if __name__ == "__main__":
    ## WiFi setup
    wifi = WiFi('ESP-CircuitSpecialists')

    ## Stepper Control
    motor = stepper.MOTOR()