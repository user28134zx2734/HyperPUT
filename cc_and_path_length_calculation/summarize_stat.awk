#================================================================================================
#
#  FILE:
#      summarize_stat.awk 
#
#  DESCRIPTION:
# 	Calculate several statistics for a list of values in a file delimited by newline	
#
#  USAGE:
#	cat <input_file> | awk -f summarize_stat.awk
#
#================================================================================================



BEGIN {
	# Field separator
	FS=" "
	line=""
	line_num=0

	# Initial values	
	max=0
	max2=0
	min=99999999999
	min2=9999999999
	avr=0
	var=0
	var2=0
}
{
	val=$1
	if (val>max)  
		max=val
	else if (val>max2)
		max2=val

	if (val < min)  
		min=val
	else if (val < min2)
		min2=val	

	avr=avr+$1
	var=var+$1
	var2=var2+($1*$1)

	line_num=line_num+1
}

END {
	avg=avr/line_num
	var=(var2/line_num) - ((var/line_num)*(var/line_num)) 

	print "MAX: " max
	print "MAX2: " max2
	print "MIN: " min
	print "MIN2: " min2
	printf "AVG: %ld\n", avg
	printf "VAR: %ld\n", var
	printf "STD DEV: %f\n", sqrt(var)
	print "PUTs: " line_num
}
