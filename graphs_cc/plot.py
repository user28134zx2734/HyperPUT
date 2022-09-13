#!/usr/bin/python3

#================================================================================================
#
#  FILE:
#      	plot.py 
#
#  DESCRIPTION:
#	Plot cyclomatic complexity graph
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

WORKDIR="graphs_cc"
show=True


# write additional column to file1
file1=WORKDIR+"/lava_cc2.sorted"
data=pan.read_csv(file1,sep=" ") 
data['Benchmark']="LAVA-1"
data.to_csv(file1 + "_2",sep=",", header=False,index=False)

# write additional column to file2
file2=WORKDIR+"/cgc_cc.sorted"
data2=pan.read_csv(file2,sep=" ") 
data2['Benchmark']="CGC"
data2.to_csv(file2 + "_2",sep=",", header=False,index=False)

# write additional column to file3
file3=WORKDIR+"/HyperPUT_cc.sorted"
data3=pan.read_csv(file3,sep=" ") 
data3['Benchmark']="HyperPUT"
data3.to_csv(file3 + "_2",sep=",", header=False,index=False)

# merge files
os.system("awk '{print $0}' cgc_cc.sorted_2 lava_cc2.sorted_2 HyperPUT_cc.sorted_2 > total_cc.csv")

file_merged=WORKDIR+"/total_cc.csv"
merged=pan.read_csv(file_merged,sep=",",names=["cc","Benchmark"]) 

merged[meds.index].boxplot(patch_artist=True, by="Benchmark")	

print(merged)


figure, ax=plt.subplots()
benchmarks=["HyperPUT", "CGC", "LAVA-1"]

position=0
for benchmark in benchmarks: 
	merged_bench=merged[merged["Benchmark"]==benchmark]
	box=ax.boxplot(merged_bench["cc"],positions=[position],patch_artist=True) 
	position=position+1

	for element in ['boxes']:#, 'whiskers', 'fliers', 'medians', 'caps']:
		plt.setp(box[element],color="#004f9e")

ax.set_xticklabels(benchmarks)
ax.set_yticks([])


plt.title(None)
plt.suptitle(None)
plt.yscale('log')
plt.xticks(rotation=55)
plt.xlabel("Benchmark")
plt.ylabel("Cyclomatic complexity")
plt.savefig(WORKDIR + str("/merged_cc") + '.png',bbox_inches='tight')
plt.savefig(WORKDIR + str("/merged_cc") + '.jpg',bbox_inches='tight')
if show == True:
	plt.show()
