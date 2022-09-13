#!/usr/bin/python3

#================================================================================================
#
#  FILE:
#       visualize.py
#
#  DESCRIPTION:
#       Display csv files. 
#
#  USAGE:
#       ./visualize.py
#
#================================================================================================

import numpy as num
import pandas as pan
import matplotlib.pyplot as plt
import seaborn as sea
import sys
import os

WORKDIR="test_out"



### Utility functions ###

def replace_names(l):

	for i in range(0,len(l)):
		if l[i]=="k":
			l[i]="KLEE"
		elif l[i]=="a":
			l[i]="AFL++"
		elif l[i]=="c":
			l[i]="CBMC"
		elif l[i]=="z":
			l[i]="ZZUF"
		elif l[i]=="ad":
			l[i]="AFL+"
		elif l[i]=="ab":
			l[i]="AFL-"
	return l 


def list_to_str(l):
    s=""
    for el in l:
        s = s + str(el) + " "
    s.rstrip()
    
    return s


def merge(file_list,outfile):
    'Merge CSV files for different testing framewoks'

    data=[]
    for f in file_list:
        print("Processing " + str(f) )
        data.append(pan.read_csv(f,sep=" "))

    for i in range(0,len(data)):
        data[i]['File']=testing_framework[i]
        data[i].info()
        data[i].describe()

    merged=pan.concat(data) 
 
    print(merged)
    merged.to_csv(outfile,sep=" ",index=False)



def merge2(file1,file2,outfile):
    'Merge CSV files for different tools (alternative implementation)'

    data1=pan.read_csv(file1,sep=" ") 
    data2=pan.read_csv(file2,sep=" ")

    data1['File']='a'
    data2['File']='k'

    merged=pan.concat([data1,data2])

    merged.to_csv(outfile,sep=" ",index=False)



def merge_columns(ifile,outcsv):
    'Merge transformation name columns into a single one'

    # read input from file1
    data=pan.read_csv(ifile,sep=" ") 

    tmp=data.copy()
    

    # save transformation columns
    end_col=ntransformations
    for i in range(0,ntransformations):
        tmp.pop("Parameters" + str(i))
        tmp.pop("Argument_number" + str(i))
    tmp['Transformations']=tmp[tmp.columns[0:end_col]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)


    merged_col=data
    merged_col['Transformations']=tmp['Transformations'] 

    # write output to outfile
    merged_col.to_csv(outcsv,sep=" ",index=False)





def display(csv_file):
    'Generate graphs'

    data=pan.read_csv(csv_file, sep=" ")
    
    # Result comparison
    if niter == 4:
        data=data.sort_values(['File','Result']) #,ascending=['False','False'])

        figure=sea.scatterplot(x='Transformations', y='Result', style=data['File'], size=data['File'], hue=data['File'], palette={"k":"Orange", "a":"#004f9e", "ab":"green", "ad":"#c91616", "z":"lightblue", "c":"black"}, data=data)
        plt.xticks([])
    else:
        data=data.sort_values('Result')
        figure=sea.barplot(x='Transformations', y='Result', hue=data['File'], palette={"k":"Orange", "a":"#004f9e", "ab":"green", "ad":"#c91616", "z":"lightblue", "c":"black"}, data=data)

    plt.xticks(rotation=77)
    plt.xticks(fontsize="7")
    plt.xlabel("Transformation category")
    
    h,l=figure.get_legend_handles_labels()	
    l=replace_names(l)
    figure.legend(h,l,title="Configuration")

    plt.savefig(outpath + '/res_cmp' + str(ntransformations) + '.jpg',bbox_inches='tight')
    plt.savefig(outpath + '/res_cmp' + str(ntransformations) + '.png',bbox_inches='tight')
    plt.savefig(outpath + '/res_cmp' + str(ntransformations) + '.svg',bbox_inches='tight')

    if show == True:
       plt.show()


    # Time comparison
    data=data.sort_values(['File','Time']) #,ascending=['False','False'])
    print(data)
    if niter == 4:
        figure=sea.lineplot(x='Transformations', y='Time', hue=data['File'], style=data['File'], size=data['File'], palette={"k":"Orange", "a":"#004f9e", "ab":"green", "ad":"#c91616", "z":"lightblue", "c":"black"}, sizes={"k":3,"a":2,"c":1}, dashes={"k":(2,2),"a":(1,0.5),"c":(3,3)}, data=data)
    else:
        figure=sea.barplot(x='Transformations', y='Time', hue=data['File'], palette={"k":"Orange", "a":"#004f9e", "ab":"green", "ad":"#c91616", "z":"lightblue", "c":"black"}, data=data)
    # logarithmic scale
    plt.yscale('log')
    plt.xticks([])
    plt.xticks(rotation=55)
    plt.xlabel("Transformation category")

    h,l=figure.get_legend_handles_labels()	
    l=replace_names(l)
    figure.legend(h,l,title="Configuration")

    plt.savefig(outpath +'/time_cmp' + str(ntransformations) + '.png',bbox_inches='tight')
    plt.savefig(outpath +'/time_cmp' + str(ntransformations) + '.jpg',bbox_inches='tight')
    plt.savefig(outpath +'/time_cmp' + str(ntransformations) + '.svg',bbox_inches='tight')
    if show == True:
                plt.show()


    # Time Result tradeoff
    if niter == 4:
        # same size for points
        figure=sea.scatterplot(x='Result', y='Time', legend="brief", hue=data['File'], style=data['File'], alpha=0.9, palette={"k":"Orange", "a":"#004f9e", "ab":"green", "ad":"#c91616", "z":"lightblue", "c":"black"}, data=data)
    else:
        # different size
        figure=sea.scatterplot(x='Result', y='Time', legend="brief", hue=data['File'], style=data['File'],size =data['File'], alpha=0.9, palette={"k":"Orange", "a":"#004f9e", "ab":"green", "ad":"#c91616", "z":"lightblue", "c":"black"}, data=data)
    plt.xticks(rotation=45)
#   plt.yscale('log')

    h,l=figure.get_legend_handles_labels()	
    l=replace_names(l)
    figure.legend(h,l,title="Configuration")

    plt.xlabel("Average result")
    plt.savefig(outpath +'/tradeoff' + str(ntransformations) + '.png',bbox_inches='tight')
    plt.savefig(outpath +'/tradeoff' + str(ntransformations) + '.jpg',bbox_inches='tight')
    plt.savefig(outpath +'/tradeoff' + str(ntransformations) + '.svg',bbox_inches='tight')
    if show == True:
    	plt.show()


def modify(ifile,outfile):
    'Modify dataset for visualization purposes'    

    data=pan.read_csv(ifile,sep=" ") 

    # make data categorical
    for column in ["Transformation_name0","File"]: 
        data[column]=pan.Categorical(data[column])

    # employ percentages instead of scalar numbers
    data['Result']=data['Result'].astype(int)
    data["Result"]=(data["Result"]/niter)*100

    data.to_csv(outfile,sep=" ",index=False)




def display_time_repetition(ifile,transformation_type=""): 
    'Generate graphs for tests with repetition'
    
    data=pan.read_csv(ifile,sep=" ") 
   
    data['N']=data['N'].astype(int)
   
    # print dataset information   
    data.info()
    data.describe() 

    # Time comparison data
    data=data[data['N']<=10]

    # matplotlib   
    for tf in testing_framework:
	    # select marker color for testing framework tf 
 	    tf_data=data[data['File']==tf]
 	    tf_data['Color']=tf_data['Result'].apply(lambda elem: "silver" if (elem==0) else tf_color[tf])
	    # print line
 	    plt.plot(tf_data['N'],tf_data['Time'], color=tf_color[tf], linewidth=2.5)
            # print points
 	    figure=plt.scatter(x=tf_data['N'],y=tf_data['Time'],marker=".",c=tf_data["Color"],linewidths=5)

   # plt.plot(data['N'],data['Time'])
    plt.xlabel("PUT size")
    plt.ylabel("Time")

    plt.savefig(outpath +'/result_rep' + str(transformation_type) + str(ntransformations) + '.png',bbox_inches='tight')
    plt.savefig(outpath +'/result_rep' + str(transformation_type) + str(ntransformations) + '.jpg',bbox_inches='tight')
    plt.savefig(outpath +'/result_rep' + str(transformation_type) + str(ntransformations) + '.svg',bbox_inches='tight')

    if show == True:
        plt.show()

   


### Main program ### 


# Global variables
path=WORKDIR 
outpath=WORKDIR + "/graphs"

# Output files for combinations 
outfile=outpath+'/output.csv'
outfile2=outpath+'/output2.csv'
outfile3=outpath+'/output3.csv'

# Number of iterations for every test
niter=10

# Show output graphs
show=True

# Testing frameworks    
testing_framework=['a','k','c']
tf_color={"k":"Orange", "a":"#004f9e", "ab":"green", "ad":"#c91616", "z":"lightblue", "c":"black"}

# combinations
for ntransformations in [1,2,7,10]:  
    if ntransformations>=7:
        niter=4
    else:
        niter=10
    
    # input files
    file_a=path+'/comb'+str(ntransformations)+'_7.csv'
    file_k=path+'/comb'+str(ntransformations)+'_k_7.csv'
    file_c=path+'/comb'+str(ntransformations)+'_c_7.csv'
    
    if ntransformations>=7:
        file_list=[file_a,file_k,file_c]
    else:
        file_list=[file_a,file_k,file_c] 

    merge(file_list,outfile)
    modify(outfile,outfile2)
    merge_columns(outfile2,outfile3) 
    display(outfile3)


file_re_list=["", "_k", "_c"] 


# string repetition
print("string repetition")
for ntransformations in [1,2,3,4]:
    
    # generate input file_list    
    file_list=[]
    for file_ in file_re_list:
        if ntransformations==1:
            filename=path+'/comb_rep' + file_ + '_2.csv'
        else:
            filename=path+'/comb_rep' + str(ntransformations) + file_ + '_2.csv'
        file_list.append(filename)

    outfile=outpath+'/output_re' + str(ntransformations) + '.csv'
    merge(file_list,outfile)
    display_time_repetition(outfile) 

# integer repetition
print("integer repetition")
for ntransformations in [1,2,3,4]:
    
    # generate input file_list    
    file_list=[]
    for file_ in file_re_list:
        if ntransformations==1:
            filename=path+'/comb_repi' + file_ + '_2.csv'
        else:
            filename=path+'/comb_repi' + str(ntransformations) + file_ + '_2.csv'
        file_list.append(filename)

    outfile=outpath+'/output_rei' + str(ntransformations) + '.csv'
    merge(file_list,outfile)
    display_time_repetition(outfile,"i") 


# wac repetition
print("wac repetition")
for ntransformations in [1,2,3,4]:
    
    # generate input file_list    
    file_list=[]
    for file_ in ["", "_k", "_c"]:
        if ntransformations==1:
            filename=path+'/comb_repw' + file_ + '_2.csv'
        else:
            filename=path+'/comb_repw' + str(ntransformations) + file_ + '_2.csv'
        file_list.append(filename)

    outfile=outpath+'/output_rew' + str(ntransformations) + '.csv'
    merge(file_list,outfile)
    display_time_repetition(outfile,"w") 



# fcc repetition
print("fcc repetition")
for ntransformations in [1,2,3,4]:
    
    # generate input file_list    
    file_list=[]
    for file_ in ["", "_k", "_c"]:
        if ntransformations==1:
            filename=path+'/comb_repf' + file_ + '_2.csv'
        else:
            filename=path+'/comb_repf' + str(ntransformations) + file_ + '_2.csv'
        file_list.append(filename)

    outfile=outpath+'/output_ref' + str(ntransformations) + '.csv'
    merge(file_list,outfile)
    display_time_repetition(outfile,"f") 



# ccc repetition
print("ccc repetition")
for ntransformations in [1,2,3,4]:
    
    # generate input file_list    
    file_list=[]
    for file_ in ["", "_k", "_c"]:
        if ntransformations==1:
            filename=path+'/comb_repc' + file_ + '_2.csv'
        else:
            filename=path+'/comb_repc' + str(ntransformations) + file_ + '_2.csv'
        file_list.append(filename)

    outfile=outpath+'/output_rec' + str(ntransformations) + '.csv'
    merge(file_list,outfile)
    display_time_repetition(outfile,"c") 



# rand repetition
print("rand repetition")
for ntransformations in [1,2,3,4]:
    
    # generate input file_list    
    file_list=[]
    for file_ in ["", "_k", "_c"]:
        if ntransformations==1:
            filename=path+'/comb_reprand' + file_ + '_2.csv'
        else:
            filename=path+'/comb_reprand' + str(ntransformations) + file_ + '_2.csv'
        file_list.append(filename)

    outfile=outpath+'/output_repr' + str(ntransformations) + '.csv'
    merge(file_list,outfile)
    display_time_repetition(outfile,"r") 




# PUT distribution

colors=["#004f9e","#004f9e","#004f9e","#004f9e", "#004f9e","#004f9e","#004f9e"]
categ=["1","2", "5", "7","10","100","1000"]
values=[10,28,100,100,100,100,100]

plt.bar(categ,values,color=colors)
plt.xlabel("PUT size")
plt.ylabel("Number of instances")
plt.savefig(outpath + '/PUT_distribution' + '.png',bbox_inches='tight')
plt.savefig(outpath + '/PUT_distribution' + '.jpg',bbox_inches='tight')
plt.savefig(outpath + '/PUT_distribution' + '.svg',bbox_inches='tight')
if show == True:
        plt.show()



# PUT distribution without 5 transformations

colors=["#004f9e","#004f9e","#004f9e", "#004f9e","#004f9e","#004f9e"]
categ=["1","2","7","10","100","1000"]
values=[10,28,100,100,100,100]

plt.bar(categ,values,color=colors)
plt.xlabel("PUT size")
plt.ylabel("Number of instances")
plt.savefig(outpath + '/PUT_distribution2' + '.png',bbox_inches='tight')
plt.savefig(outpath + '/PUT_distribution2' + '.jpg',bbox_inches='tight')
plt.savefig(outpath + '/PUT_distribution2' + '.svg',bbox_inches='tight')
if show == True:
        plt.show()



# PUT distribution with merged batches 

colors=["#004f9e","#004f9e","#004f9e", "#004f9e","#004f9e","#004f9e"]
categ=["1","2","3","4","5","6","7","8","9","10","100","1000"]
values=[10,46,6,10,46,75,92,108,110,36,100,100]


plt.bar(categ,values,color=colors)
plt.xlabel("PUT size")
plt.ylabel("Number of instances")
plt.savefig(outpath + '/PUT_distribution3' + '.png',bbox_inches='tight')
plt.savefig(outpath + '/PUT_distribution3' + '.jpg',bbox_inches='tight')
plt.savefig(outpath + '/PUT_distribution3' + '.svg',bbox_inches='tight')
if show == True:
        plt.show()

