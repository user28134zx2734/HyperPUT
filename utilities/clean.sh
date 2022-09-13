#!/bin/bash

#================================================================================================
#
#  FILE:
#	clean.sh
#
#  DESCRIPTION:
#	Clean environment and remove temporary files
#
#  USAGE:
#	chmod u+x ./utilities/clean.sh
#	./utilities/clean.sh
#
#================================================================================================


USER="user"
WORKDIR=/home/$USER/Desktop/PUT_generator_v0.407


clean() {
	cd "$WORKDIR"	
	echo "Cleaning directory..."
	for file_ in *.tmp tmp a.out progr.c.test.c* progr*.c_transformed.c* progr*.c_transformed.c.* progr.c.test.c* *.png stdout stderr.txt transformation.list_final output*.csv;  do
		rm "$file_" 2>/dev/null
	done
	echo "Done"
}


dir="$(pwd)"
if [[ "$dir" != "$WORKDIR" ]]; then
	echo "The script must be run from the work directory "$WORKDIR""
	echo "Current directory: $dir"
	exit 1
fi

clean
