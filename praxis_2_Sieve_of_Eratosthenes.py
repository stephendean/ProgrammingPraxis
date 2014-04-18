# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 16:35:05 2014

Sieve of Eratosthenes
February 19, 2009

[...]

Write a function that takes a single argument n and returns a list of 
prime numbers less than or equal to n using the optimized sieving algorithm 
described above. Apply the function to the argument 15485863 and count the 
number of primes returned.

@author: Stephen
"""

def sieve1(n):
    primes = [2]
    sv = set()
    for x in xrange(3, n+1, 2):
        if x not in sv:
            if x*x <= n+1:
                sv.update(xrange(x*x, n+1, x))
            primes.append(x)
            
    return primes


P = sieve1(15485863)

print P[:50]
print len(P)