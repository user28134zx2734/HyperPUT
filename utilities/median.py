#/usr/bin/python3

#================================================================================================
#
#  FILE:
#       median.py
#
#  DESCRIPTION:
#       Calculate the median given a file consisting of a list of values delimited by newline. 
#
#  USAGE:
#       python3 median.py <input-file>
#
#================================================================================================



import statistics
import sys

if len(sys.argv) > 1:
	filename=sys.argv[1]
	file1=open(filename, 'r')	

	list1=[]
	for line in file1:
		line1=line.strip()
		if line1[0].isnumeric(): 
			value = float(line1)
			list1.append(value)

	list1.sort()
	m=statistics.median(list1)
	print("List: ", list1)
	print("Median: ", m)
else:
	print("Error")
