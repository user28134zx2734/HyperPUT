#!/bin/bash

#================================================================================================
#
#  FILE:
#	test_input.sh
#
#  DESCRIPTION:
#	Execute a PUT with the corresponding triggering input provided by HyperPUT.
#
#  USAGE:
#	chmod u+x test_input.sh
# 	./test_input.sh <put_file_name_without_extension>
#
#================================================================================================

COMPILER="gcc"
# With Valgrind
#VALGRIND_cmd="valgrind --tool=cachegrind --branch-sim=yes" 
# Without Valgrind (default)
VALGRIND_cmd="" 


PUT="$1"

if [[ -f "$PUT".c && -f "$PUT"_input ]]; then
	echo "Compiling..."
	"$COMPILER" "$PUT".c

	echo "Executing..."
	A="$(cat "$PUT"_input )" && $VALGRIND_cmd ./a.out $A
	echo "Done."
else
	echo "Provided PUT path does not exist. Exiting..."	

fi
