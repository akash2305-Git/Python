#!/bin/python3

import math
import os
import rando

class Car :
    def __init__(self,max_speed,min_speed):
        self.x = max_speed
        self.y = min_speed
        
    def main(car):
        if max_speed > min_speed:
            print('Car {} km/h'.format(max_speed))

        else :
            print('car {} mph'.format(min_speed))
c =Car(151,95)
print(c.main)

class Boat :
    def __init__(self,speed):
        self.speed = speed

    def speed(Boat):
        s = print('boat {} speed'.foramt(speed))

b =Boat(77)
print(b.speed)




