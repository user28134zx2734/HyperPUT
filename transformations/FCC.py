#!/usr/bin/python3


#================================================================================================
#
#  FILE:
#       FCC.py
#
#  DESCRIPTION:
#       Generate valid inputs for transformation FCC.
#
#================================================================================================


import os, sys

valid_char="c"
param=int(sys.argv[1])

output=""
for i in range(0,param):
	output=output+valid_char			

print(output + " ")
