#!/usr/bin/python3 

#================================================================================================
#
#  FILE:
#       test.py
#
#  DESCRIPTION:
#       Generate list of transformations and apply them to produce batches of PUTs.
#
#  USAGE:
#       python3 test.py
#
#================================================================================================

import itertools
import sys
import os
import subprocess
import random

import utilities.config
from utilities.config import *


# MAIN SETTINGS (read from config.py)
fin=COMB_FILE
fout=COMB_FILE + "_final"

workdir=WORKDIR
framework=FRAMEWORK

# Number of iterations for every combination
num_it=NUM_IT


# SECONDARY SETTINGS (specific for this file)

# Temporary file to hold normalized configuration file
tmp="tmp"

# Stop after max_put_n generated PUTs; 0=no limit
max_put_n=MAX_PUT_NUM

# Skip first num_to_skip PUTs; 0=disabled
num_to_skip=0

# Skip PUTs with less than threshold transformations; 0=disabled
threshold=0 # 6 
# Skip PUTs with more than max_transform transformations; 0=disabled
max_transform=0 #8

# Initial seed for prng
initial_seed=70973249532165074

# Number of PUT to generate for predefined options
PUT_num=max_put_n


def str_to_list(s):
    l=[]
    for el in s.split():
        l.append(el)
    return l


def list_to_str(l):
    s=""
    for el in l:
        s = s + str(el) + " "
    s.rstrip()
    
    return s


# add quotes to string
def quote(s):
    return "\""+str(s)+"\""


# remove quotes from string
def dequote(s):
    return str(s).replace("\"","")


# Apply permutation contained in 'perm' list to the elements of 'in_list'
def apply_perm(in_list, perm):
    
    if len(in_list) != len(perm):
        print("Error: lists must have the same length. Exiting...")
        return -1

    out_list=[]

    for i in range(0,len(in_list)):
        out_list.append(in_list[perm[i]])

    return out_list


def print_options():
    print("\n\n\n\n")
    print("#########################################")
    print("\nHyperPUT v0.407.")
    print("#########################################")
    print("\n\n\n\n")
    print("Configuration files:\n")
    print("1. utilities/config.py: Main program settings.\n")
    print("2. transformation.list: List of transformations to apply with corresponding input sources and parameters.\n")
    print("\n\n\n\n")




def print_intro():
    print("\n\n\n\n")
    print("#########################################")
    print("\nHyperPUT v0.407.")
    print("#########################################")
    print("\n\n\n\n")

def initialize():
    subprocess.call(["./utilities/initialize.sh", framework, workdir] )



def execute_transformation():
    subprocess.call(["./transform.sh", framework, str(TIMEOUT), PUT_FOLDER, FINAL_TRANSFORMATION])


def normalize():
    'Remove comments and newlines'
    with open(fin,'r') as fdin:
        with open(tmp,'w') as fdout:
            for line in fdin:
                if not(line.startswith("#")) and line != "" and line != " " and line != "\n" :
                   fdout.write(line)  



# Generate parameters for a specific transformation when employing random parameter strategy.
def get_param(transformation,index):
    # SC-SC2
    if transformation[0] == "sc" or transformation[0] == "sc2" :    
        return "\""+str(random.randint(1,int(transformation[index].replace("\"",""))))+"\""    
    else:    
        return random.randint(1,int(transformation[index].replace("\"","")))    
            

#'Generate a PUT. Parameters:
#    -cmd_args:  Choose argument numbers. 
#        Options
#        'file': Choose from file.
#        'sequence': Use sequence of arguments from 1 to number of transformations
#        'n'(integer value): Use selected command line argument'

def gen_test(): 
    'Generate a list of transformations to test'

    random.seed(initial_seed)

    with open(tmp,'r') as fdin:
            lines=fdin.read().split('\n')

            # remove trailing empty element, if present 
            try:
                lines.remove("")
            except ValueError:
                pass

            print("LINES: " + str(lines))

            # count the number of combinations or more specifically, the number of generated PUTs
            u=1

# test single transformation mode: test single transformation multiple times (with random parameters)
#.a         for transformation in itertools.combinations(lines,1):
#.a             for tests in range(0,50):

            ## for every single line
#.0         for transformation in itertools.combinations(lines,1):   

            ## for every combination of lines 
            # no order, no repetition
#.1         for transformation in itertools.combinations(lines,2):   
            # order, no repetition
#.2         for transformation in itertools.permutations(lines,5):
            # order, repetition
#.3         for transformation in itertools.product(lines,repeat=10):#len(lines)):
            # pairwise combination with repetition
#.4         for transformation in itertools.product(lines,repeat=2):#len(lines)):

            # previous 7 transformations: order, repetition, jump, 100 deterministic iterations
            #for transformation in itertools.islice(itertools.product(lines,repeat=7),1,sys.maxsize,485000):

            # 7 transformations
            for t_count in range(0,PUT_num):#.5
                transformation=random.choices(lines,k=7)#.5


#.6         for transformation in itertools.islice(itertools.product(lines,repeat=5),1,sys.maxsize,10):   
            # previous 10 transformations
            #for transformation in itertools.islice(itertools.product(lines,repeat=10),80000001,sys.maxsize,850000000):

            # 10 transformation transformations
#.7         for t_count in range(0,PUT_num):   
#.7             transformation=random.choices(lines,k=10)   

            # 100 transformations
#.8         for t_count in range(0,PUT_num):   
#.8             transformation=random.choices(lines,k=99)   


            # 1000 transformations
#.d         for t_count in range(0,PUT_num):   
#.d             transformation=random.choices(lines,k=1000)   


            # same transformation repeated multiple times
#.9         for transformation in [[lines[0]]*y for y in range(1,MAX_REP+1)]:   
            

            # Incremental PUTs with increasing length (y) and random transformations 
#.b         transformation=[]   
#.b         for y in range(2,MAX_REP+1):   
#.b            for vz in range(0,y):   
#.b             line_index=random.randint(0,len(lines)-1)   
#.b             transformation.extend([lines[line_index]])   

            # Random PUTs with increasing length (y) and random transformations 
#.c         transformation=[]   
#.c         for y in range(1,MAX_REP+1):   
#.c             transformation=[]   
#.c             for vz in range(0,y):   
#.c                 line_index=random.randint(0,len(lines)-1)   
#.c                 transformation.extend([lines[line_index]])   




                # write PUT transformation list to file
                with open(fout,'w') as fdout:
                    for i in range(0,len(transformation)):
                        
                        new_transformation=transformation[i].split()
                        
                        # update args -> modification doesn't work on tuples -> use list
                        
                        # -cmd arguments from file: comment the following lines
                        # -cmd arguments: 1 2 3 4 5 ...
                        new_transformation[1]=i+1#a.1
                        # -cmd arguments: 1 1 1 1 1 ...
#a.2                    new_transformation[1]=1    

                        # -parameters from file: comment the following lines
                        # - increasing cmd arguments
#b.1                    tmp_var=new_transformation[2]    
#b.1                    dequoted=dequote(new_transformation[2])    
#b.1                    new_transformation[2]=int(dequoted)+i    
#b.1                    if dequoted != tmp_var:    
#b.1                            new_transformation[2]=quote(new_transformation[2])    
                        # - increasing cmd argument length
#b.2                    new_transformation[2]=int(new_transformation[2])*pow(10,i)    
                        # random parameters
                        for z in range(2,len(new_transformation)):#b.3
                            new_transformation[z]=get_param(new_transformation,z)#b.3

                        fdout.write(list_to_str(new_transformation))
                        fdout.write("\n")

                 

                # skip first num_to_skip PUTs
                if u<=num_to_skip:
                    print("Skipping PUT number " + str(u) + "\n")
                    u=u+1
                    continue

                # skip PUT if number of effective transformations (not none) is less than threshold or more than max_transform
                length=len(transformation)
                for elem in transformation:
                    if elem.startswith("none"):
                        length=length-1 
               
                if (threshold != 0 and length<threshold): 
                    print("Skipping PUT number " + str(u) + ". (Number of transformations: " + str(length)+ ". Minimum required : "+str(threshold)+")","\n")
                    u=u+1
                    continue
 
                if (max_transform != 0 and length>max_transform):
                    print("Skipping PUT number " + str(u) + ". (Number of transformations: " + str(length)+ ". Maximum required : "+str(max_transform)+")","\n")
                    u=u+1
                    continue
 

 
                # Repeat test num_it times
                for j in range(0,num_it):

                    # debug
                    print("\n====Generating PUT number:", str(u), "\n") 
                    print("\nExecuting the following transformation:\n") 
                    with open(fout,'r',newline='') as fdout:
                        for line in fdout:
                            print(line, end='')

                    #update_args()

                    # execute it 
                    execute_transformation()

                if (max_put_n==0 or u<max_put_n):
                    u=u+1
                else:
                    print("Number of generated PUTs: ", str(u))
                    return 0
                    
            print("Number of generated PUTs: ", str(u-1))


if len(sys.argv)>1 and sys.argv[1]=="-h":
    print_options()
else:
    print_intro()
    initialize()
    normalize()
    gen_test()
