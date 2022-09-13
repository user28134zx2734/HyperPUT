#!/bin/bash

#================================================================================================
#
#  FILE:
#	conversion.awk
#
#  DESCRIPTION:
#	Convert CSV output file.
#
#  USAGE:
#	awk -f conversion.awk <file>
#
#================================================================================================


BEGIN  {
	# INPUT VARIABLE: number of test repetitions
	#n=10

	# field separator
	FS=" "

	# line number
	ln=1

	# average time
	avt=0

	# average number of successes
	av=0	

	# success value (1 or 0 in the Result column indicating success)
	sv=1
}

 
{ 	
	# update avt
	avt=avt+$(NF-1)

	# update av
	if ($NF==sv)
		av=av+1

	# print av and avt field
	if ((ln%n)==0) {
		print $0 " " avt/n " " av # "/"n
		avt=0
		av=0
	}

	# increment line number
	ln=ln+1
}


END {
	
}


