#Get the highest mountain

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while 1: #while 1 means while true to run continuous loop
    max = 0
    imax = 0
    for i in range(8):
        mountain_h = int(input()) # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
        if mountain_h > max:
            max = mountain_h
            imax = i

    print(imax)