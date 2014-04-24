# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 10:09:05 2014

The Digits of Pi
February 20, 2009


The ratio of the circumference of a circle to its diameter is given by the 
constant known by the Greek letter pi, and is an irrational number 
(its representation is non-terminating and non-repeating) with a value 
slightly larger than 3.14159. What is the one-thousandth digit 
of pi? (Counting begins at zero, so the zeroth digit of pi is 3 and the 
fourth digit of pi is 5.)

@author: Stephen
"""

import decimal

def PiDigit(m):
    '''return the nth digit of pi'''
    if m<0:
        return -1
    
    decimal.getcontext().prec = m+2
    
    #this block taken from https://docs.python.org/2/library/decimal.html#recipes
    #reciples for the decimal module    
    
    three = decimal.Decimal(3)
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t    
        
    
    s = str(s)
    s = s[0] + s[2:] #remove the decimal point
    return s[m]

print PiDigit(1000)
print PiDigit(4)