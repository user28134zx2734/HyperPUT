#!/usr/bin/python3

#================================================================================================
#
#  FILE:
#      	plot.py 
#
#  DESCRIPTION:
#	Plot path length graph
#
#  USAGE:
#      python3 plot.py 
#
#================================================================================================


import numpy as num
import pandas as pan
import matplotlib.pyplot as plt
import seaborn as sea
import sys
import os

WORKDIR="graphs_path_length"
show=True

# write additional column to file1
file1=WORKDIR+"/lava_tracelen.txt_sorted"
data=pan.read_csv(file1,sep=" ") 
data['Benchmark']="LAVA-1"
data.to_csv(file1 + "_2",sep=",", header=False,index=False)

# write additional column to file2
file2=WORKDIR+"/hyperput_tracelen.txt_sorted"
data2=pan.read_csv(file2,sep=" ") 
data2['Benchmark']="HyperPUT"
data2.to_csv(file2 + "_2",sep=",", header=False,index=False)

# merge files
os.system("awk '{print $0}' lava_tracelen.txt_sorted_2 hyperput_tracelen.txt_sorted_2 > total_tracelen.csv")

file_merged=WORKDIR+"/total_tracelen.csv"
merged=pan.read_csv(file_merged,sep=",",header=None,names=["Trace_Length","Benchmark"]) 

## standard boxplot
figure= merged.boxplot(patch_artist=True, by="Benchmark")

## display
plt.title(None)
plt.suptitle(None)
plt.yscale('log')
#plt.xticks([])
plt.xticks(rotation=55)
plt.xlabel("Benchmark")
plt.ylabel("Trace length")
plt.savefig(WORKDIR + str("/merged_tracelength") + '.png',bbox_inches='tight')
plt.savefig(WORKDIR + str("/merged_tracelength") + '.jpg',bbox_inches='tight')
if show == True:
	plt.show()

