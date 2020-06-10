#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys
import os
import random
import datetime

def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))
    p = sys.platform
    print(p)
    n = os.name
    print(n)
    e = os.getenv('PATH')
    print(e)
    c = os.getcwd()
    print(c)
    r = os.urandom(25)
    print(r) #get 25 bytes
    h = os.urandom(25).hex()
    print(h)
    x = random.randint(1,1000)
    print(x)
    l = list(range(25))
    print(l)
    random.shuffle(l)
    print(l)
    now = datetime.datetime.now()
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)

if __name__ == '__main__': main()
