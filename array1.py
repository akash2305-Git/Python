#!/bin/python3

import math
import os
import random
import re
import sys
import array
# Complete the compareTriplets function below.
pa=pb=0
def compareTriplets(a, b):
    
    if a[0]>b[0]:
        pa +=1
    elif a[0]<b[0]:
        pb +=1
    elif a[1]>b[1]:
        pa +=1
    elif a[1]<b[1]:
        pb +=1
    elif a[2]>b[2]:
        pa +=1
    elif a[2]<b[2]:
        pb +=1
    else:
        pa = pb =0
    
    return pa,pb
        

a = array('i',[])
append.array(a)
b = arrat('j',[])
append.array(b)

    
