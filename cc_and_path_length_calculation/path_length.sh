#!/bin/bash

#================================================================================================
#
#  FILE:
#      path_length.sh 
#
#  DESCRIPTION:
# 	Calculate path length for every Program Under Test and the corresponding inputs
#
#  USAGE:
#	chmod u+x ./path_length.sh
#       ./path_length.sh
#
#================================================================================================



PUT_DIR=puts
PUTS_SUBDIR=("$PUT_DIR"/one "$PUT_DIR"/two  "$PUT_DIR"/seven "$PUT_DIR"/ten "$PUT_DIR"/one-hundred "$PUT_DIR"/challenging)

OUTFILE="put_stats_outfile"

rm "$OUTFILE"*  || echo ""

set -e

for d in "${PUTS_SUBDIR[@]}"; do
	for f in "$d"/*.c ; do
		echo "Processing ""$f"" ..."
		rm tmp || echo ""
		rm tmp2 || echo ""
		rm a.out || echo ""

		# Compile	
		gcc -Wall "$f" 

		# Save input
		dir="$(dirname "$f")"
		in_file="${f%.c}"_input
		IN="$(cat "$in_file")" 
	
		# Test input	
		set +e
		{ valgrind --tool=cachegrind --branch-sim=yes ./a.out $IN ; } &> tmp
		{ valgrind --tool=cachegrind --branch-sim=yes ./a.out $IN ; } &> tmp2

		# Write to file
		echo "$f" >> "$OUTFILE"1
		echo "$f" >> "$OUTFILE"2
		egrep "I\ *refs" tmp | egrep -o ":\ +[0-9]*,?[0-9]*,[0-9]*" | sed -E 's/:\ *//' >> "$OUTFILE"1 
		egrep "Branches" tmp2 | egrep -o ":\ +[0-9]*,?[0-9]*,[0-9]*" | sed -E 's/:\ *//' >> "$OUTFILE"2

		echo "" >> "$OUTFILE"1
		echo "" >> "$OUTFILE"2
			
		set -e
	done
done
