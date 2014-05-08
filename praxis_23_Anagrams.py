# -*- coding: utf-8 -*-
"""
Created on Thu May 08 12:24:12 2014

http://programmingpraxis.com/2009/04/10/anagrams/

Words that are formed from the same set of letters are anagrams of each other. 
For instance, pots, post, stop, spot, opts, and tops are anagrams.

Your task is to write a program that, given a dictionary and an input word, 
prints all the anagrams of the input word. You are also to determine the 
largest anagram class in your dictionary. 

@author: Stephen
"""

    
def Anagrams(d, w):
    '''Find all anagrams of word w in dictionary d'''
    
    ANAGRAMS = {}
    
    f = open(d)
    
    for line in f:
        line = line.strip()
        line = line.split()
        word = line[0] #text file containes definitions which are excised
        word = word.upper()
        wordlist = list(line[0])
        wordlist.sort()
        key = ''.join(wordlist)
    
        if key in ANAGRAMS:
            ANAGRAMS[key].append(word)
        else:
            ANAGRAMS[key] = [word]
            
    
    f.close()
    
    w = w.upper() #dictionary is allcaps
    ws = list(w)
    ws.sort()
    ws = ''.join(ws)
    
    if ws in ANAGRAMS and len(ANAGRAMS[ws])>1:
        print ws, "Anagrams of " + w + ": " + str(ANAGRAMS[ws])
    else:
        print w + " has no anagrams in this dictionary."
    
    largest = 2
    large_key = ''
    for k in ANAGRAMS:    
        if len(ANAGRAMS[k]) > largest:
            largest = len(ANAGRAMS[k])
            large_key = k
    
    
    print "Largest class of anagrams for this dictionary: " + str(ANAGRAMS[large_key])    
    
Anagrams("OWL2.txt", 'epigon')