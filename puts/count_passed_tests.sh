#!/bin/bash

#================================================================================================
#
#  FILE:
#	count_passed_tests.sh
#
#  DESCRIPTION:
#	Count total number of passed tests for PUTs of length <LENGTH>.
#
#  USAGE:
#	chmod u+x count_passed_tests.sh 
#	./count_passed_tests.sh <LENGTH>
#
#================================================================================================


LOG_DIR=/home/user/Desktop/PUT_generator_v0.407/test_out
LENGTH="$1"

set -e

for f in $LOG_DIR/comb"$LENGTH"*.csv; do

	if [[ ! -f "$f" ]]; then
		echo "File ""$f" "does not exist. Exiting..."
		exit -1
	fi

	echo "Processing ""$f"" ..."

	# Consider only passed tests
	PASSED="$(cat $f | egrep -v " 0$" | uniq)"
	
	# echo "$PASSED"

	# Calculate number of passed tests
	N_PASSED="$(echo "$PASSED" | wc -l)"

	echo "$f"
	echo "$N_PASSED"
done
