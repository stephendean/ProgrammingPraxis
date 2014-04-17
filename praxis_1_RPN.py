# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 12:43:24 2014

http://programmingpraxis.com/2009/02/19/rpn-calculator/

Problem Description:

RPN Calculator
February 19, 2009
Implement an RPN calculator that takes an expression like 
19 2.14 + 4.5 2 4.3 / - * which is usually expressed as 
(19 + 2.14) * (4.5 - 2 / 4.3) and responds with 85.2974. 

The program should read expressions from standard input and print the top of 
the stack to standard output when a newline is encountered. The program 
should retain the state of the operand stack between expressions.

@author: Stephen
"""

OPS = {'+': lambda x,y : x+y,
       '-': lambda x,y : x-y,
       '*': lambda x,y : x*y,
       '/': lambda x,y : x/y}

def eval_rpn(exp):
    o = len([i for i in exp if i in OPS])
    if o != len(exp) - o - 1:
        return "Error! Improper expression"
    stack = []
    for token in exp:
        if token in OPS:
            try:
                b = stack.pop()
                a = stack.pop()
                c = OPS[token](a, b)
                stack.append(c)
            except IndexError:
                return "Error! Improper expression"
            except ZeroDivisionError:
                return "Error! Division by zero"
        else:
            try:
                stack.append(float(token))
            except:
                return "Error! " + str(token) + " is not a number"
    
    return stack.pop()

while True:
    expression = raw_input("Enter expression (q to quit): ")
    
    if expression != 'q':
        print eval_rpn(expression.split())
    else:
        break
        
