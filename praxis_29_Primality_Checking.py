# -*- coding: utf-8 -*-
"""
Created on Wed May 07 12:47:35 2014

http://programmingpraxis.com/2009/05/01/primality-checking/

In a previous exercise you wrote a function that returned a list of prime 
numbers, and in another exercise you used that function to find a particular 
prime number. This exercise looks at prime numbers from a different 
perspective by considering a function that takes a number and determines 
if it is prime.

The algorithm that we will consider was developed initially by Gary Miller 
and refined by Michael Rabin, and is probabilistic in nature. It works like 
this: Express the odd number n to be factored as n = (2^r)s + 1 with s odd. 
Then choose a random integer a with 1 ≤ a ≤ n-1 and check if as ≡ 1 (mod n) 
or a^(2^j) s ≡ -1 (mod n) for some 0 ≤ j ≤ r-1. (Some browsers render that last 
equation poorly; it’s a raised to the power 2 to the j times s.) A prime 
number will pass the check for all a. A composite number will pass the check 
for about 1/4 of the possible as and fail the check for the remaining 3/4 of 
the possible as. Thus, to determine if a number n is prime, check multiple as; 
if k as are checked, this algorithm will err less than one time in 4k. Most 
primality checkers set k to somewhere between 25 and 50, making the chance of 
error very small.

Your task is to write a function that determines if an input number n is prime, 
then to determine if 2^89-1 is prime.

@author: Stephen
"""

def Miller_Rabin(n, k=25):
    '''Miller-Rabin Primality Test for n, ran k times'''
    if n==2:
        return True
    if n%2==0:
        return False
    #Express the odd number n to be factored as n = (2^r)s + 1 with s odd
    s = n-1
    r = 0
    while s%2==0:
        s/=2
        r+=1
    
    from random import randint
    
    
    for i in xrange(k):
        
        a = randint(1, n-1) #choose a random integer a with 1 ≤ a ≤ n-1
        passed = False
        
        if pow(a, s, n) ==1: #check if as ≡ 1 (mod n) ...
            passed = True
        else:
            for j in xrange(0, r): #for some 0 ≤ j ≤ r-1
                exponent = (2**j)*s
                if pow(a,exponent,n) == n-1: #... or a^(2^j) s ≡ -1 (mod n)
                    passed = True
                    break
        
        if not passed:
            return False
    
    return True


#primes from 2 to 100
primes_list = [i for i in xrange(2,100) if Miller_Rabin(i)]
print primes_list        

#determine if 2^89-1 is prime'
print 2**89 -1, Miller_Rabin(2**89 - 1)
