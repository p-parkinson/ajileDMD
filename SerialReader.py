# -*- coding: utf-8 -*-
# -*- python=3.8.x
"""
Created on 17/07/2023

Reads data from Arduino

@author: Alex Kedziora
"""

import serial

class ArduinoUNO:
    ser: serial.Serial

    def __init__(self,COM:str):
        self.ser = serial.Serial(COM, 115200, timeout=2)

    def Read(self):
        return self.ser.readline() # Read the data (looks for terminating character '/r/n')
    

def main():
    ar = ArduinoUNO("COM3")

    while(True):
        text = ar.Read()
        if(len(text) != 0):
            print(text)

main()