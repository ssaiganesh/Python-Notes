#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = 'This is a long string with a bunch of words in it.'
print(s.split())
print(s.split('i')) #splits on the i


l = s.split()
s2 = 'i'.join(l)
s3 = '--'.join(l)
print(s2)
print(s3)