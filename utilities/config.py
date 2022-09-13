#!/usr/bin/python3 

#================================================================================================
#
#  FILE:
#	config.py
#
#  DESCRIPTION:
#       Configuration file containing the main program settings. 
#
#  USAGE:
#       import config
#
#================================================================================================


##### Program settings #####

# Work directory.
user="user"
WORKDIR="/home/" + user + "/Desktop/PUT_generator_v0.407"

# Output folder for generated PUTs. When this variable is left empty, the produced PUTs are not saved.
PUT_FOLDER=WORKDIR+"/puts/other"

# Testing framework to employ. 
# Valid options: 'klee', 'afl', 'afl_bb', 'afl_default', 'bbrtesting', 'zzuf', ''. 
# New testing frameworks can be added to: "$WORKDIR"/transform.sh
# An empty string causes the generator to only generate PUTs and corresponding inputs, without evaluating testing frameworks.
FRAMEWORK="afl"
#FRAMEWORK="klee"
#FRAMEWORK="cbmc"
#FRAMEWORK=""

# Number of iterations for every transformation
NUM_IT=10

# Number of maximum repetitions (for repeated single transformation)
MAX_REP=10

# Timeout in seconds
# 1 min
#TIMEOUT=60
# 10 min
#TIMEOUT=600
# 60 min
TIMEOUT=3600
# 100 minutes
#TIMEOUT=6000
# 1000 minutes (about 16.67 h)
#TIMEOUT=60000

# Transformation file containing transformation list and corresponding parameters
COMB_FILE="transformation.list"

# Stop after MAX_PUT_NUM generated PUTs; 0=no limit
MAX_PUT_NUM=100

# Print debug information 2=Advanced, 1=Basic information; 0=False
DEBUG=0

# Final transformation to apply. Valid options: ASSERT_BUG, ABORT_BUG, BO_BUG.
if FRAMEWORK == "klee" or FRAMEWORK == "cbmc" or FRAMEWORK == "":   
    FINAL_TRANSFORMATION="ASSERT_BUG"
else:
    FINAL_TRANSFORMATION="ABORT_BUG"

## Strategy applied to combine transformations.
# Valid options:

                ## for every single line in the transformation file
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

                # order, repetition, 100 deterministic iterations
                # seven combinations of transformations
    #.5         for transformation in itertools.islice(itertools.product(lines,repeat=7),1,sys.maxsize,1): 
                # five combinations of transformations
    #.6         for transformation in itertools.islice(itertools.product(lines,repeat=5),1,sys.maxsize,10): 
                # ten combinations of transformations
    #.7         for transformation in itertools.islice(itertools.product(lines,repeat=10),80000000,sys.maxsize,10000000):                                        

                # 100 combinations of transformations
    #.8         for t_count in range(0,100):
    #.8             transformation=random.choices(lines,k=100)
                   
                # same transformation repeated multiple times
    #.9         for transformation in [[lines[0]]*y for y in range(1,MAX_REP+1)]:
COMB_STRATEGY="#.1"


## Choice of command line arguments. Valid choices:

                            # -cmd arguments from file
                            # #none

                            # -cmd arguments: 1 2 3 4 5 ...
                            # a.1 new_transformation[1]=i+1

                            # -cmd arguments: 1 1 1 1 1 ...
                            # a.2 new_transformation[1]=1
CMD_STRATEGY="#none"

## Choice of parameters. Valid choices:
                            # -parameters from file
                            # none

                            # -random parameters 
                            # b.3 

                            # - increasing parameters
                            # b.1 new_transformation[2]=int(new_transformation[2])+i

                            # - increasing parameter length
                            # b.2 new_transformation[2]=int(new_transformation[2])*pow(10,i)
PARAM_STRATEGY="#none"


# Default values: they must be present in order to avoid interpreter's error
DEFAULT_COMB="#.0"
DEFAULT_CMD="#a.2"
DEFAULT_PARAM="none"



# Example of settings for tests:

## Repeated transformations. Same parameter for every transformation and constant number of input arguments 
#COMB_STRATEGY="#.9"
#CMD_STRATEGY="#a.2"
#PARAM_STRATEGY="#none"
#NUM_IT=1 #10
#PUT_FOLDER=""

# File: transformation.list
#sc.cocci 1 1 or ic.cocci 1 1

## Repeated transformations. Same parameter for every transformation and increasing number of input arguments 
#COMB_STRATEGY="#.9"
#CMD_STRATEGY="#a.1"
#PARAM_STRATEGY="#none"
#NUM_IT=1 #10
#PUT_FOLDER=""

# File: transformation.list
#sc.cocci 1 1 or ic.cocci 1 1

## Repeated transformations. Different parameters for every transformation and increasing number of input arguments 
#COMB_STRATEGY="#.9"
#CMD_STRATEGY="#a.1"
#PARAM_STRATEGY="#b.1"
#NUM_IT=1 #4
#PUT_FOLDER=""
#PUT_FOLDER=WORKDIR+"/puts_final2/r3"
#PUT_FOLDER=WORKDIR+"/puts_final2/r3-i"
#PUT_FOLDER=WORKDIR+"/puts_final2/r3-wac"
#PUT_FOLDER=WORKDIR+"/puts_final2/r3-fcc"
#PUT_FOLDER=WORKDIR+"/puts_final2/r3-ccc"

# File: transformation.list
#sc 1 "1" or ic 1 1 or wac 1 181 or fcc 1 1 or ccc 1 1

## Repeated transformations. Different parameters for every transformation and increasing number of input arguments with increasing size
#COMB_STRATEGY="#.9"
#CMD_STRATEGY="#a.1"
#PARAM_STRATEGY="#b.2"
#NUM_IT=4 #10
#PUT_FOLDER=""

# File: transformation.list
#sc 1 "1" or ic 1 1


## Variable length PUTs with random transformations and random arguments. 
#COMB_STRATEGY="#.c"
#CMD_STRATEGY="#a.1"
#PARAM_STRATEGY="#b.3"
#NUM_IT=1 #4
#PUT_FOLDER=""
#PUT_FOLDER=WORKDIR+"/puts_final2/rand"

# File: transformation.list
#ic 1 255
#ic2 1 255
#ccc 1 10
#ccc2 1 10
#wac 1 255
#fac 1 255
#sc 1 "255"
#sc2 1 "255"
#fcc 1 10
#fcc2 1 10


## Combinations 1
#COMB_STRATEGY="#.0"
#CMD_STRATEGY="#a.2"
#PARAM_STRATEGY="#none" 
#NUM_IT=1# 10
#PUT_FOLDER=""
#PUT_FOLDER=WORKDIR+"/puts_final2/one"

# File: transformation.list
#ic 1 173
#ic2 1 213
#ccc 1 7
#ccc2 1 8
#wac 1 142
#fac 1 45
#sc 1 "137"
#sc2 1 "184"
#fcc 1 6
#fcc2 1 7


## Combinations 2
#COMB_STRATEGY="#.1" #.0 #.1 #.5 #.7
#CMD_STRATEGY="#a.1" #"#none"
#PARAM_STRATEGY="#none"
#NUM_IT=1 #10 
#PUT_FOLDER=""
#PUT_FOLDER=WORKDIR+"/puts_final2/two"


# File: transformation.list
#ic 1 173
#ic2 1 213
#ccc 1 7
#ccc2 1 8
#wac 1 142
#fac 1 45
#sc 1 "137"
#sc2 1 "184"
#fcc 1 6
#fcc2 1 7



## Combinations 7
COMB_STRATEGY="#.5" #.0 #.1 #.5 #.7
CMD_STRATEGY="#a.1"
PARAM_STRATEGY="#b.3"
NUM_IT=1 #4 
PUT_FOLDER=""
#PUT_FOLDER=WORKDIR+"/puts_final2/seven"

# File: transformation.list
#ic 1 173
#ic2 1 213
#ccc 1 7
#ccc2 1 8
#wac 1 142
#fac 1 45
#sc 1 "137"
#sc2 1 "184"
#fcc 1 6
#fcc2 1 7
#none 1 1

# v0.4 with random parameters from interval
#ic 1 255
#ic2 1 255
#ccc 1 10
#ccc2 1 10
#wac 1 255
#fac 1 255
#sc 1 "255"
#sc2 1 "255"
#fcc 1 10
#fcc2 1 10
#none 1 1
#none 1 1
#none 1 1



## Combinations 10
#COMB_STRATEGY="#.7" #.0 #.1 #.5 #.7
#CMD_STRATEGY="#a.1"
#PARAM_STRATEGY="#b.3"
#NUM_IT=1 #1
#PUT_FOLDER=""
#PUT_FOLDER=WORKDIR+"/puts_final2/ten"


# File: transformation.list
# v0.4 with random parameters from interval
#ic 1 255
#ic2 1 255
#ccc 1 10
#ccc2 1 10
#wac 1 255
#fac 1 255
#sc 1 "255"
#sc2 1 "255"
#fcc 1 10
#fcc2 1 10
#none 1 1
#none 1 1
#none 1 1



## Combinations 20
#COMB_STRATEGY="#.8" #.0 #.1 #.5 #.7
#CMD_STRATEGY="#a.1" 
#PARAM_STRATEGY="#none"
#NUM_IT=1 #4
#PUT_FOLDER=WORKDIR+"/puts/twenty"


## Combinations 100
#COMB_STRATEGY="#.8" #.0 #.1 #.5 #.7
#CMD_STRATEGY="#a.1"
#PARAM_STRATEGY="#b.3"
#NUM_IT=1 #4
#PUT_FOLDER=WORKDIR+"/puts_final2/one-hundred"
#PUT_FOLDER="" 

# File: transformation.list
# v0.4 with random parameters from interval
#ic 1 255
#ic2 1 255
#ccc 1 10
#ccc2 1 10
#wac 1 255
#fac 1 255
#sc 1 "255"
#sc2 1 "255"
#fcc 1 10
#fcc2 1 10


## Challenging short PUTs
#COMB_STRATEGY="#.8" #.0 #.1 #.5 #.7
#CMD_STRATEGY="#a.1"
#PARAM_STRATEGY="#none"
#NUM_IT=1 #4

# File: transformation.list
# ic2.cocci 1 100
# fcc2.cocci 1 100


## Challenging PUTs
#COMB_STRATEGY="#.d" #.0 #.1 #.5 #.7
#CMD_STRATEGY="#a.1"
#PARAM_STRATEGY="#b.3" #"#none"
#NUM_IT=1 #4
#PUT_FOLDER=WORKDIR+"/puts_final2/challenging"

# File: transformation.list
# v0.02
# 1000 trasformations
#ic2 1 1000
#sc2 1 "1000"
#fcc2 1 300

# v0.4 with random parameters from interval

#ic 1 255
#ic2 1 255
#ccc 1 10
#ccc2 1 10
#wac 1 255
#fac 1 255
#sc 1 "255"
#sc2 1 "255"
#fcc 1 10
#fcc2 1 10


## Test from file
#COMB_STRATEGY="#.0"
#CMD_STRATEGY="#none"
#PARAM_STRATEGY="#none"
#NUM_IT=1 #4


##########################





##### Program code  ######


import sys


def reset_all(filename):
    ''' Reset options to their default values '''

    with open(filename,'r+') as infile:
            lines=infile.readlines()
            infile.seek(0)
            infile.truncate()

            comb_options=["#."+str(n) for n in range(0,10)]
            comb_options.extend(["#."+str(n) for n in ["a","b","c","d","e","f"]])
            cmd_options=["#a."+str(n) for n in range(0,10)]
            cmd_options.extend(["#a."+str(n) for n in ["a","b","c","d","e","f"]])
            param_options=["#b."+str(n) for n in range(0,10)]
            param_options.extend(["#b."+str(n) for n in ["a","b","c","d","e","f"]])
            comb_options.extend(comb_options)
            comb_options.extend(cmd_options)
            comb_options.extend(param_options)
         
            options=comb_options        
            for line in lines:
                for option in options:
                    if line.strip().endswith(option):
                        # remove option
                        index=line.find(option)
                        for i in range(0,len(option)):
                            lline=str_to_list(line) 
                            lline[index+i]=" "
                            line=list_to_str(lline)
                       

                        #add option at the beginning
                        for i in range(0,len(option)):
                            lline=str_to_list(line) 
                            lline[i]=option[i]
                            line=list_to_str(lline)


                infile.write(line) 


def write_options(filename,option):
    ''' Write options to file'''

    with open(filename,'r+') as infile:
        lines=infile.readlines()
        infile.seek(0)
        infile.truncate()

        for line in lines:
            if line.strip().startswith(option):

                # remove option
                index=line.find(option)
                for i in range(0,len(option)):
                    lline=str_to_list(line) 
                    lline[index+i]=" "
                    line=list_to_str(lline)

                # add option at the end
                line=line[:len(line)-1].rstrip() + option + "\n"

            infile.write(line) 

def list_to_str(l):
    ''' Convert list into a string '''
    return ''.join(l) 


def str_to_list(str_):
    ''' Convert string to list '''
    return list(str_)




def main():

    # write options to file
    if DEBUG>1:
        print("Executing config.py...")
    filename=WORKDIR + "/test.py"

    if len(sys.argv)>1 and sys.argv[1]=="reset":

        # reset default values
        reset_all(filename)
        write_options(filename,DEFAULT_COMB)
        write_options(filename,DEFAULT_CMD)
        write_options(filename,DEFAULT_PARAM)

    else:
        reset_all(filename)
        write_options(filename,COMB_STRATEGY)
        write_options(filename,CMD_STRATEGY)
        write_options(filename,PARAM_STRATEGY)

#if __name__ == '__main__':
main()


###########################
