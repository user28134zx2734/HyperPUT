#!/bin/bash

#================================================================================================
#
#  FILE:
#	conversion.sh
#
#  DESCRIPTION:
#	Convert CSV output file.
#
#  USAGE:
#	chmod u+x conversion.sh 
#	./conversion.sh <WORKDIR>
#
#================================================================================================



comb() {
	# filename without extension
	filename="${FILE%.*}"

	# output files
	FILE2="$filename""_2.csv"
	FILE3="$filename""_3.csv"
	FILE4="$filename""_4.csv"
	FILE5="$filename""_5.csv"
	FILE6="$filename""_6.csv"
	FILE7="$filename""_7.csv"


	if [[ ! -f "$FILE" ]]; then
		echo "File" "$FILE" " does not exist."
		echo "Exiting..."
		exit 1
	fi

	set -e


	cp "$FILE" "$filename""_0.csv"

	# round time
	sed -i -E 's/m([0-9]+\.[0-9])[0-9]+s/m\1s/' "$FILE"
	sed -i -E 's/\s([0-9]+\.[0-9])[0-9]+/ \1/g' "$FILE"

	# get header
	header="$(head -1 "$FILE")"

	# remove empty lines and header
	awk 'BEGIN {FS=" "} ; { if (NF>2 && $NF!="Result") print $0}' "$FILE" > "$FILE2"

	# convert to seconds
	awk 'BEGIN {FS=" "} ; { if (NF>2) split($(NF-1),a,"m"); print $0 " " a[1]*60+a[2]}' "$FILE2" > "$FILE3"

	# calculate average time and average score
	awk -f "$WORKDIR""/utilities/conversion.awk" -v n="$niter" "$FILE3" > "$FILE4"

	# round time again
	sed -i -E 's/m([0-9]+\.[0-9])[0-9]+s/m\1s/' "$FILE4"
	sed -i -E 's/\s([0-9]+\.[0-9])[0-9]+/ \1/g' "$FILE4"

	# remove unused fields
	awk 'BEGIN {FS=" "} ; { for (i=1;i<=NF; i++) {if (i!=NF-2 && i!=NF-4 && i!=NF-3) printf $i " "  ;  if (i==NF) print "\n" ; }}'  "$FILE4" | awk '{$1=$1;print}' > "$FILE5"

	# reinsert header
	sed -i "1 i\'$header'" "$FILE5" 
	cat "$FILE5" | tr -d "\'" > "$FILE6" 

	# remove empty lines
	awk 'BEGIN {FS=" "} ; { if (NF>2) print $0}' "$FILE6" > "$FILE7"

}


comb_with_repetition() {
	# filename without extension
	filename="${FILE%.*}"

	# output file
	FILE2="$filename"_2.csv

	if [[ ! -f "$FILE" ]]; then
		echo "File" "$FILE" "does not exist."
		echo "Exiting..."
		exit 1
	fi

	set -e

	# backup file
	cp "$FILE" "$filename""_0.csv"

	# round time
	sed -i -E 's/m([0-9]+\.[0-9])[0-9]+s/m\1s/' "$FILE"
	sed -i -E 's/\s([0-9]+\.[0-9])[0-9]+/ \1/g' "$FILE"

	# convert to seconds
	awk 'BEGIN {FS=" "; OFS=" "} ; { if (NF>2) {split($(NF-1),a,"m"); for (i=1;i<=NF-2; i++) printf "%s ", $i; print a[1]*60+a[2]" "$NF}}' "$FILE" > "$FILE".tmp


	# remove empty lines
	awk 'BEGIN {FS=" "} ; { if (NF>2) print $0}' "$FILE".tmp > "$FILE".tmp2

	# calculate average time and average score
	awk -f "$WORKDIR""/utilities/conversion2.awk" -v n="$niter" "$FILE".tmp > "$FILE2".tmp

	# round time again
	sed -i -E 's/m([0-9]+\.[0-9])[0-9]+s/m\1s/' "$FILE2".tmp
	sed -i -E 's/\s([0-9]+\.[0-9])[0-9]+/ \1/g' "$FILE2".tmp

	# save time
	awk 'BEGIN {FS=" "; i=6} ; { print  NR" "$i" "$(i+1) ; i=i+3}' "$FILE2".tmp > "$FILE2".tmp2

	# add header
	header="N Time Result"
	sed -i "1 i\'$header'" "$FILE2".tmp2
	cat "$FILE2".tmp2 | tr -d "\'" > "$FILE2" 

	# remove tmp file
	rm "$FILE".tmp
	rm "$FILE".tmp2
	rm "$FILE2".tmp

}







WORKDIR="$1"

# combinations of transformations
# input file list
file_list=("1_c" "1" "1_k" "2" "2_k" "2_c" "7" "7_k" "7_c" "10" "10_k" "10_c")  
niter=10
for FILE in "${file_list[@]}"; do

	
        if [[ "$FILE" == "7" || "$FILE" == "7_k" ||  "$FILE" == "10" || "$FILE" == "10_k" ]]; then
        	niter=4
	else
		niter=10
        fi		

	FILE="$WORKDIR""/test_out/comb""$FILE"".csv"
	echo "Processing ""$FILE""..."
	if [[ "$(cat "$FILE")" == "" ]]; then
		echo "Warning: the file is empty."
	fi

	# remove testing framework name
	for FRAMEW in "afl" "klee" "cbmc" ; do
		sed -i "s/$FRAMEW//" "$FILE"
	done

	comb	
done


# combinations with repetition
# empty=scc i=ic, w=wac, f=fcc, rand=random, c=ccc
trasf_list=("w" "f" "i" "" "rand" "c")  
file_list=("3" "3_k" "3_c") 

for TRASF in "${trasf_list[@]}"; do
	niter=10
	if [[ "$TRASF" == "w" || "$TRASF" == "f" || "$TRASF" == "rand" || "$TRASF" == "" || "$TRASF" == "i" || "$TRASF" == "c" ]]; then
		niter=4
	fi
	for FILE in "${file_list[@]}"; do

		FILE="$WORKDIR""/test_out/comb_rep""$TRASF""$FILE"".csv"
		echo "Processing ""$FILE""..."
		if [[ "$(cat "$FILE")" == "" ]]; then
			echo "Warning: the file is empty."
		fi

		# remove testing framework name
		for FRAMEW in "afl" "klee" "cbmc" ; do
			sed -i "s/$FRAMEW//" "$FILE"
		done

		comb_with_repetition
	done
done
