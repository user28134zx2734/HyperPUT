#!/bin/bash

#================================================================================================
#
#  FILE:
#	initialize.sh
#
#  DESCRIPTION:
#	Initialize environment: verify that there is no running container
#	and write fields to CSV output file.
#
#  USAGE:
#	chmod u+x initialize.sh
#	./initialize.sh
#
#================================================================================================


# Verify there is no running container
stop_containers() {
	echo -e "Stopping containers...\n"
	"$WORKDIR"/utilities/stop_containers.sh
	echo -e "\nDone.\n"
}

# Write first line in CSV file
write_csv_field_names() {
	FIELDS=('Transformations_name' 'Argument_number' 'Parameters')

	# number of transformations
	N="$(wc -l "$LIST" | awk '{print $1}' )"

	echo -e "\n\n\n\n" >> "$CSV_FILE"
	for (( i=0; i < $N; i++ )); do
		for el in '${FIELDS[@]}'; do
			echo -e -n "Transformation_name""$i" "Argument_number""$i" "Parameters""$i"" " >> "$CSV_FILE"
		done
	
	done 
	echo -e -n "Time " >> "$CSV_FILE"
	echo -e -n "Result" >> "$CSV_FILE"
}

write_csv_framework_name() {
	echo >> "$CSV_FILE"	
	echo >> "$CSV_FILE"	
	echo "$FRAMEWORK" >> "$CSV_FILE"		
}


prepare_files() {
	echo -e "Preparing files...\n"
	"$WORKDIR"/utilities/conversion.sh "$WORKDIR"
	echo -e "Done.\n"
}


set -e

FRAMEWORK="$1"
WORKDIR="$2"

if [[ "$FRAMEWORK" == "" || "$WORKDIR" == "" ]]; then
	echo Missing arguments:
	echo "$0" " <framework> <workdir> "
	echo "Exiting..."
fi


LIST="$WORKDIR""/transformation.list_final"
CSV_FILE="$WORKDIR""/transform.sh.csv"


stop_containers
write_csv_framework_name
write_csv_field_names
prepare_files
