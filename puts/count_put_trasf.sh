#!/bin/bash

#================================================================================================
#
#  FILE:
#	count_put_trasf.sh
#
#  DESCRIPTION:
# 	Calculate number of effectively applied transformations without considering the empty one
#
#  USAGE:
#	chmod u+x count_put_trasf.sh
#	./count_put_trasf.sh
#
#================================================================================================


# Empty transformation name
TRASF="NONE"
# Folder 
FOLDER="seven"
# Number of total transformations in chosen folder
NUM_TRASF_TOT=7

cd "$FOLDER"
cat *_trasf | awk -F "$TRASF" '{ print NF-1 }' | sort | uniq -c | awk -F " " '{print $1" "7-$2}'
cd ..
