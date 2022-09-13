#!/bin/bash

#================================================================================================
#
#  FILE:
#	count_trasf.awk
#
#  DESCRIPTION:
#	Count the number of transformations.
#
#  USAGE:
#	awk -f count_trasf.awk
#
#================================================================================================


BEGIN  {

	# INPUT VAR: number of test repetitions
	#n=10 or 4
	
	# field separator
	FS=" "

	# line number
	ln=1

	# number of matches for each line
	n[]
}

 
{ 	
	# print av and avt field
	if ($0 ~ NONE) {	
		n[ln]=n[ln]+1
	}

	# increment line number
	ln=ln+1
}


END {
	for elem in n
		print n":"elem
	
}


