#!bin/bash

#================================================================================================
#
#  FILE:
#	put_stats2.sh
#
#  DESCRIPTION:
# 	Calculate the following dynamic metrics on the generated PUTs with the corresponding input: 
#
#				-Number of testcases produced by KLEE before detecting the bug.
#
#  USAGE:
#	cd <HYPERPUT_DIR>
#	chmod u+x <HYPERPUT_DIR>/utilities/put_stats2.sh
#	<HYPERPUT_DIR>/put_stats2.sh
#
#
#================================================================================================

HYPERPUT_DIR="/home/user/Desktop/PUT_generator_v0.407"
PUT_DIR=/home/user/Desktop/puts
PUTS_SUBDIR=("$PUT_DIR"/ten) 


# stop running containers
$HYPERPUT_DIR/utilities/initialize.sh "k"

# removing old files
rm $HYPERPUT_DIR/klee-output/klee_test_num_tot.txt || echo "Proceeding..."


for d in "${PUTS_SUBDIR[@]}"; do
	for f in "$d"/*.c ; do
		echo "Processing ""$f"" ..."
		./transform.sh "$f"  
	done
done
