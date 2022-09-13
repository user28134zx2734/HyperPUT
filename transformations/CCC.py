#!/usr/bin/python3


#================================================================================================
#
#  FILE:
#       CCC.py
#
#  DESCRIPTION:
#       Generate valid inputs for transformation CCC.
#
#================================================================================================


import os, sys, random, math

param=int(sys.argv[1])

if param<=0:
    param=1

length=param

half_palindrome=""
for i in range(0,math.ceil(length/2)):
    half_palindrome=half_palindrome+str(random.randint(0,9))
palindrome=half_palindrome
for char in reversed(half_palindrome):
    palindrome=palindrome+char
    
print (palindrome + " ")
