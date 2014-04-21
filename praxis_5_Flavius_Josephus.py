# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 11:18:10 2014

Flavius Josephus
February 19, 2009

Flavius Josephus was a famous Jewish historian of the first century, 
at the time of the destruction of the Second Temple. According to legend, 
during the Jewish-Roman war he was trapped in a cave with a group of forty 
soldiers surrounded by Romans. Preferring death to capture, the Jews decided 
to form a circle and, proceeding around it, to kill every third person 
remaining until no one was left. Josephus found the safe spot in the circle 
and thus stayed alive.

Write a function josephus(n,m) that returns a list of n people, numbered 
from 0 to n-1, in the order in which they are executed, every mth person in 
turn, with the sole survivor as the last person in the list. What is the 
value of josephus(41,3)? In what position did Josephus survive?

@author: Stephen
"""


def josephus(n, m):
    L = []
    stack = range(n)
    pos = 1
    while len(stack) > 1:
        p = stack.pop(0)
        if pos%m==0: #killed
            L.append(p)
        else: #not killed --> back in the stack
            stack.append(p)
        pos+=1
    
    return L+[stack[0]]


print josephus(41, 3)