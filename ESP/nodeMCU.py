#!/usr/bin/python
"""
written by Jake Pring from CircuitSpecialists.com
licensed as GPLv3
"""

import machine

class ESP8266:
    def __init__(self):
        # actual pin markings
        #self.S3 = self.GPIO10
        #self.S2 = self.GPIO9
        self.D0 = 16
        self.D1 = 5
        self.D2 = 4
        self.D3 = 0
        self.D4 = 2
        self.D5 = 14
        self.D6 = 12
        self.D7 = 13
        self.D8 = 15
        self.A0 = 17