#!/bin/bash

#================================================================================================
#
#  FILE:
#      	cccc.sh 
#
#  DESCRIPTION:
# 	Calculate cyclomatic complexity and statistics for every file in a folder
#
#  USAGE:
#	chmod u+x ./cccc.sh
#       ./cccc.sh
#
#================================================================================================



FOLDER=""
SUBFOLDER_LIST="one two seven ten one-hundred challenging" 
OUTFILE="cccc-out.txt"
AWK_STAT_FILE="summarize_stat.awk"

set -e

# remove old files
rm "$OUTFILE" "$OUTFILE"_final || true

for d in $SUBFOLDER_LIST; do
	FOLDER="$d"
	for f in $FOLDER/*.c; do
		cc="$(pmccabe "$f" | awk '{print $2}')"
		echo "$f" >> "$OUTFILE"
		echo "$cc" >> "$OUTFILE"
		echo  >> "$OUTFILE"
	done
done
egrep "^[0-9]+" "$OUTFILE" | awk -f "$AWK_STAT_FILE"  > "$OUTFILE"_final
