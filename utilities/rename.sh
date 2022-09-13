#!/bin/bash

#================================================================================================
#
#  FILE:
#	rename.sh
#
#  DESCRIPTION:
#	Rename transformation files.
#
#  USAGE:
#	chmod u+x rename.sh
#	./rename.sh
#
#================================================================================================



WORKDIR=~/Desktop/PUT_generator/
cd "$WORKDIR"/transformations/

for f in *.cocci; do
	# insert header with filename	
	#sed -i "1 i\\/\/$f" "$f" 

	# rename
	nf="$(echo "$f" |  awk 'BEGIN{RS="_"} {printf("%c", $1) ; if (index($1,'2')!=0) printf("%d",2); if (index($1,'3')!=0) printf("%d",3);} END{print(".cocci")}')"
	echo "$f" 
	echo "$nf"
	mv "$f" "$nf"

done


