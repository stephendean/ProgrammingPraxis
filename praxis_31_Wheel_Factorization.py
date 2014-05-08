# -*- coding: utf-8 -*-
"""
Created on Thu May 08 14:57:17 2014

http://programmingpraxis.com/2009/05/08/wheel-factorization/

Your second task is to write a function that finds the factors of a given 
number using wheel factorization; you should compute and use a 2,3,5,7-wheel. 
What are the factors of 600851475143? 

@author: Stephen
"""

PRIMES = [2,3,5,7]

def build_wheel(P):
    c = reduce(lambda x,y: x*y, P) #wheel circumference
    wheel = range(1, c)
    
    for x in P:
        wheel = [i for i in wheel if i%x != 0]
        
    return c, wheel
    
def isPrime(n):
    if n==1:
        return False
        
    ceiling = int(n**0.5)
    
    for x in xrange(2, ceiling+1):
        if n%x==0:
            return False
    return True
    
    
fullwheel = build_wheel(PRIMES)


def wheel_factorization(n, wheel):
    circumference, spokes = wheel
    
    ceiling = int(n**0.5)
    factors = []
    #test primes
    factors = [i for i in PRIMES if n%i==0]
    
    
    for s in spokes:
        turns = 0
        while s + turns*circumference <= ceiling:
            a = s + turns*circumference
            if n%a == 0:
                factors.append(a)
                
            turns+=1
        
    factors.sort()
    
    #check remaining for primality
    return [i for i in factors if isPrime(i)]
    

print wheel_factorization(600851475143, fullwheel)
    
    