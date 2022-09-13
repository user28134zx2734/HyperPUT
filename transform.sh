#!/bin/bash

#================================================================================================
#
#  FILE:
#	transform.sh
#
#  DESCRIPTION:
# 	Execute list of program transformations in configuration file. 
#
#  USAGE:
#	chmod u+x transform.sh
#	./transform.sh
#
#================================================================================================


WORKDIR="/home/user/Desktop/PUT_generator_v0.407"

FOLDER="$WORKDIR""/transformations"

# Folder to save puts
PUT_FOLDER="$3" 

# Initial PUT
C_FILE="$WORKDIR""/program.c"
# Generated PUT
C_FILE2="$C_FILE""_transformed.c"
INCLUDE_FILE="$WORKDIR"/"includes.h"

LIST="$WORKDIR""/transformation.list"
# timeout in seconds
TIMEOUT="$2"

# Compiler 1
CC1=gcc
# Compiler 2 (if present)
CC2=clang

# Print debug information 2=Advanced debug, 1=Basic information; 0=False
DEBUG=1

# Transformations to apply
COMPILER_TRANSFORMATIONS=""
# Complete list of possible transformations that can be applied
COMPILER_TRANSFORMATION_LIST="-floop-unroll-and-jam -Ofast"
FLAGS="-Wall " 

# Output options: "csv" or "multiline"
OUT_FORMAT="csv"
CSV_FILE="$WORKDIR""/transform.sh.csv"

# Testing framework. Valid options: 'klee', 'afl', 'bbrtesting', 'zzuf'.
FRAMEWORK="$1"

# Testing frameworks header files
A_HEAD=""$WORKDIR"/initial_progr/argv-fuzz-inl.h"

# Final transformation to apply
FINAL_TRANSFORMATION="$4"



## Utility functions ##

apply_compiler_transformations() {
	FLAGS+="$COMPILER_TRANSFORMATIONS"
}


update_csv() {
	if [[ "$OUT_FORMAT" == "multiline" ]]; then
		echo >> "$CSV_FILE"
		echo >> "$CSV_FILE"
		echo "Transformation:" >> "$CSV_FILE"
		cat "$LIST"_final >> "$CSV_FILE"
	else
		echo >> "$CSV_FILE"
		echo >> "$CSV_FILE"
		cat "$LIST"_final | tr '\n' ' ' >> "$CSV_FILE"
	fi	
}


# Apply all the transformations defined in LIST, replacing their symbolic arguments every time
apply_transformations() {
	## build string
	transformation="$(awk -v seed=$RANDOM -v rand_param=0 -v final_transformation="$FINAL_TRANSFORMATION" -v initial_transformation="INIT(" -f "$WORKDIR"/utilities/list_to_func.awk "$LIST"_final)"
	
	if [[ "$DEBUG" == "1" ]]; then
		echo "TRANSFORMATION: ""$transformation"
	fi
	
	## write to file
	# clean previous tmp files
	rm "$C_FILE2".tmp* || echo

	echo "$transformation""}" >> "$C_FILE2".tmp 

	cat "$C_FILE" "$C_FILE2".tmp > "$C_FILE2".tmp2

	set +e
	# preprocess (and remove include directives)
	{ $CC1 -x c -E -nostdinc -P "$C_FILE2".tmp2 > "$C_FILE2".tmp3 ; } 2>/dev/null
	set -e
		
	# add include directives again
	cat "$INCLUDE_FILE" "$C_FILE2".tmp3 > "$C_FILE2"

	if [[ "$DEBUG" == 1 ]]; then
		# compile	
		$CC1 $FLAGS "$C_FILE2"  
		echo	
	fi
}




# Get an input to cause the bug
get_input() {
	INPUT=""
	while IFS= read -r line; do

		param="$(echo "$line" | awk '{print $3}')"" "
		tname="$(echo "$line" | awk '{print $1}' | tr 'a-z' 'A-Z')"
		tfile="$FOLDER"/"$tname".py 
		if [[ "$DEBUG" == 2 ]]; then
			echo "$tfile"
		fi

		# Use script to generate tranformation-specific inputs
		if [[ -f "$tfile" ]]; then
			INPUT+="$("$tfile" "$param")"

		# Default: use the parameter as input
		elif [[ "$line" != "" ]]; then
			INPUT+="$param"
		else
			echo "Input generation error."
			touch input_gen_err
		fi

	done < "$LIST"_final

	if [[ $DEBUG > 1 ]]; then
	 	echo "INPUT: "
		echo "$INPUT"
	fi

} 



# Compile PUT in order to calculate coverage
calculate_cov() {
	FLAGS+=" -fprofile-arcs --coverage -ftest-coverage"

}

# Save collected coverage information
save_cov() {
	OUTF="cov.out"
	echo "$C_FILE".test.c"$n_puts" >> "$OUTF" 
	gcov -b "$C_FILE".test.c | grep Branches | sed 's/.*://' | tr -d '%' | awk '{print $1*$3/100}' >> "$OUTF" 
	echo >> "$OUTF"
}


# Test the generated input
test_input() { 
	if [[ "$DEBUG" == 2 ]]; then
		echo "FLAGS:" "$FLAGS"
	fi
	cp "$C_FILE2" "$C_FILE".test.c
	$CC1 $FLAGS "$C_FILE".test.c
	if [[ "$?" != 0 ]]; then
		echo "Compilation error."
		touch comp_err2
	fi

	echo "INPUT: ""$INPUT"
	./a.out $INPUT > /dev/null
	
	RET="$?"
	if [[ "$DEBUG" == 1 ]]; then
		echo "RETURN CODE: ""$RET"
		if [[ "$PUT_FOLDER" != "" ]]; then
			echo "RETURN CODE: ""$RET" >  "$PUT_FOLDER"/"put_""$n_puts"_ret	
		fi
	fi
}


# Test the generated input with multiple compilers and perform at the same time differential testing of them
test_input_multiple_compilers() {
	
	if [[ "$DEBUG" == 1 ]]; then
		echo "INPUT: ""$INPUT"
	fi

	cp "$C_FILE2" "$C_FILE".test.c

	$CC1 -fsanitize=undefined $FLAGS "$C_FILE".test.c
	if [[ "$?" != 0 ]]; then
		echo "Compilation error."
		touch comp_err2
	fi

	./a.out $INPUT > /dev/null
	RES1="$?"
	OUT1="$(./a.out $INPUT 2>&1 | tail -c 27)"
	echo "out1: ""$OUT1" 

	$CC2 -fbracket-depth=5000 -fsanitize=undefined $FLAGS "$C_FILE".test.c
	if [[ "$?" != 0 ]]; then
		echo "Compilation error."
		touch comp_err3
	fi

	./a.out $INPUT  > /dev/null
	RES2="$?"
	if [[ "$RES1" != "$RES2" ]]; then
		echo "Compilation error."
		touch comp_err4
		echo RES1 >> comp_err4
		echo RES2 >> comp_err4
	fi


	OUT2="$(./a.out $INPUT 2>&1 | tail -c 27 )"
	echo "out2: ""$OUT2"
	
	if [[ "$OUT1" != "$OUT2" ]]; then
		touch comp_err1
		echo "Possible bug found: the two outputs are different!"
		echo "out1:" >> comp_err1
		echo "$OUT1" >> comp_err1
		echo "out2:" >> comp_err1
		echo "$OUT2" >> comp_err1
	fi
}


start_container() {
	docker run -d --rm -ti --ulimit='stack=-1:-1' klee/klee

	sleep 1.5
	ID="$(docker ps | awk '{if ($1 != "CONTAINER") print $1}')"
	
	if [[ "$ID" == "" ]]; then
		echo "Error. Exiting..."
		exit
	fi

	docker ps

	if [[ "$DEBUG" == 2 ]]; then
		echo docker cp "$WORKDIR" "$ID:/home/klee"
	fi
	docker cp "$WORKDIR" $ID:/home/klee
	
	if [[ "$DEBUG" == 2 ]]; then
		echo docker cp "$C_FILE2" "$ID:/home/klee"
	fi
	docker cp "$C_FILE2" "$ID:/home/klee"
}



stop_container() {
	docker stop $ID

	IDs="$(docker ps | awk '{if ($1 != "CONTAINER") print $1}')"

	for id in $IDs; do
		docker stop $id
	done
}


# Analyze (and backup) log produced by KLEE
klee_check_assertion_fail() {
	string_to_match="ASSERTION FAIL" 
	grep_out="$(fgrep -m 1 -o "$string_to_match" "$KLEE_OUT_DIR"/stdout)"
	if [[ "$grep_out" == "$string_to_match" ]]; then
		RES=1
		echo "Bug found"
	else
		RES=0
	fi	

	# backup output for additional analyses 
	transformation_id="$(echo "$transformation" | tr -d "(),\"")"
	log_file="$KLEE_OUT_DIR"/stdout_"${transformation_id:0:100}"
	if [[ -f "$log_file" ]]; then
		cp "$KLEE_OUT_DIR"/stdout "$log_file"_2 
	else
		cp "$KLEE_OUT_DIR"/stdout "$log_file"
	fi
}


# Use klee on the generated program
test_klee() {
	echo "Testing with KLEE..."

	KLEE_OUT_DIR="$WORKDIR"/klee-output
	# Allow second configuration on failure
	ALLOW_SECOND_CONFIG="yes"

	mkdir "$KLEE_OUT_DIR" || echo "Proceeding..."

	echo "Initializing container and copying files..."
	start_container
	PROGR_NAME="$(basename "$C_FILE2")"
	docker exec "$ID" cp /home/klee/"$PROGR_NAME" test.c
	echo "Done."

	echo -n "Compiling source into llvm bytecode... "
	docker exec "$ID" clang -fbracket-depth=5000 $FLAGS -g -emit-llvm -c test.c -o test.bc
	echo "Done"

	echo "Analyzing PUT..."
	set +e	
	
	# default
	{ time docker exec "$ID" timeout "$TIMEOUT" klee  -solver-backend=stp -optimize-array=all -solver-optimize-divides --optimize --libc=uclibc --exit-on-error --posix-runtime --ignore-solver-failures --all-external-warnings  --emit-all-errors --search=random-state -max-stack-frames=0 test.bc --sym-args 1 11 30 ; } &> "$KLEE_OUT_DIR"/stdout #10 10 15 #11 11  # 1 21 50

	# if test fails, try other combination of options
	klee_check_assertion_fail

	if [[ "$RES" == 0 && "$ALLOW_SECOND_CONFIG" == "yes" ]]; then
		echo "Retrying with different options..."
		# default
		{ time docker exec "$ID" timeout "$TIMEOUT" klee --optimize --libc=uclibc --exit-on-error --posix-runtime --ignore-solver-failures --all-external-warnings  --emit-all-errors --search=random-state test.bc --sym-args 10 21 2  ; } &> "$KLEE_OUT_DIR"/stdout 
		klee_check_assertion_fail
	fi
	cp "$KLEE_OUT_DIR"/stdout "$WORKDIR"

	write_csv "$RES"
	
	if [[ "$DEBUG" == 2 ]]; then
		# print output
		cat stdout
	fi


	# Remove comments for additional output
	# print options	
	#docker exec "$ID" klee-stats --help
	# print stats
	#docker exec "$ID" klee-stats --print-all klee-last
	docker exec "$ID" klee-stats --to-csv klee-last > "$KLEE_OUT_DIR"/klee_stats.csv
	docker exec "$ID" klee-stats klee-last > "$KLEE_OUT_DIR"/klee_stats2.csv
	docker exec "$ID" cat klee-last/info > "$KLEE_OUT_DIR"/klee_info.txt
	#docker cp "$ID"":/home/klee/stats.csv" .

	# save total number of test cases before the detection
	docker exec "$ID" ls -f klee-last | grep \.ktest | wc -l >  "$KLEE_OUT_DIR"/klee_test_num.txt
	#docker exec "$ID" cat klee-last/info | grep "generated test" | awk '{print $6}' > "$KLEE_OUT_DIR"/klee_test_num.txt
	echo "$C_FILE2"" ""$transformation" >> "$KLEE_OUT_DIR"/klee_test_num_tot.txt
	cat "$KLEE_OUT_DIR"/klee_test_num.txt >> "$KLEE_OUT_DIR"/klee_test_num_tot.txt
	echo >> "$KLEE_OUT_DIR"/klee_test_num_tot.txt

	# save total number of triggering test cases
	echo "$C_FILE2"" ""$transformation"  >> "$KLEE_OUT_DIR"/klee_nttest_cases.txt
	#docker exec "$ID" ls -alH klee-last | grep \.assert\.err | wc -l >>  "$KLEE_OUT_DIR"/klee_nttest_cases.txt
	docker exec "$ID" ls -f klee-last | grep \.assert\.err | wc -l >>  "$KLEE_OUT_DIR"/klee_nttest_cases.txt
	echo >> "$KLEE_OUT_DIR"/klee_nttest_cases.txt

	# attach to container
	#docker cp "$C_FILE2" "$ID:/home/klee"
	#docker attach "$ID"

	stop_container

	set -e
}

zzuf_framework() {
	count=0
	while true; do
		count=$((count+1))
		# Alternative options
		#{ zzuf -dddd -vvv -B 2 </dev/zero | xargs -0 ./a.out ; } &> tmp_out
		{ zzuf -dddd -vvv -r1  </dev/zero | xargs -0 ./a.out ; } &> tmp_out
		TMP_OUT="$(<tmp_out)"
		if [[ "$TMP_OUT" =~ "terminated" ]]; then
			echo "1"
			echo "$count" > tmp_out2
			return 1
		fi
 	done
}


test_zzuf() {
	export -f zzuf_framework

	cp "$C_FILE2" test.c
	$CC1 $FLAGS test.c

	set +e	
	RES=0
	{ time timeout "$TIMEOUT" bash -c zzuf_framework ; } &> stdout
		
	RES="$?"
	write_csv "$RES"
	
	if [[ "$DEBUG" == 2 ]]; then
		# print output
		cat stdout
	fi

	set -e
}


# black-box random testing
bbrtesting() {
	while true; do cat /dev/urandom | xargs -0 ./a.out ; done;
	# Alternative implementation
	#while true; do head -c 10 /dev/urandom | xargs -0 ./a.out ; done;
}


test_bbrtesting() {
	export -f bbrtesting

	cp "$C_FILE2" test.c
	$CC1 $FLAGS test.c

	set +e	
	trap -- "" SIGABRT ; { time timeout "$TIMEOUT" bash -c bbrtesting ; } &> stdout 

	RES="$?"
	echo "$RES"
	
	write_csv "$RES"

	set -e
}



# clean previous afl run	
clean_afl() {
	rm -r in out || true
	mkdir in out 
	echo a >> in/in1
}


test_afl() {
	cd "$WORKDIR"

	if [[ ! -d afl ]]; then
		mkdir afl
	fi

	cd afl
	rm test.c || true
	touch test.c
		
	# modify source code
	while IFS="" read -r line; do
		echo "$line" >> test.c
		if [[ "$line" =~ '#include <stdlib.h>' ]]; then
			echo "#include \""$A_HEAD"\"" >> test.c
		elif [[ "$line" =~ 'int main(int argc, char* argv[])' ]]; then
			echo "AFL_INIT_SET0(\"a.out\");" >> test.c
		fi
	done < "$C_FILE2"	

	clean_afl

	# compile
	AFL_LLVM_CMPLOG=1 AFL_LLVM_LAF_ALL=1 afl-clang-fast -fbracket-depth=5000 $FLAGS test.c 

	set +e

	{ time AFL_NO_UI=1 AFL_BENCH_UNTIL_CRASH=1 AFL_EXPAND_HAVOC_NOW=1  AFL_DISABLE_TRIM=1 afl-fuzz -d -L 0 -t 10 -m none -V "$TIMEOUT" -i in -o out ./a.out ; } &> stdout 
	# check if directory out/crashes contains a new file
	[[ "$(ls -f out/crashes)" != "" ]];

	RES="$?"
	if [[ "$RES" == 1 ]]; then
		clean_afl
		echo "Retrying with different options..."
		{ time AFL_NO_UI=1 AFL_BENCH_UNTIL_CRASH=1 AFL_DISABLE_TRIM=1 afl-fuzz -d -p coe -t 5 -m none -V "$TIMEOUT" -i in -o out ./a.out ; } &> stdout

		# check if directory out/crashes contains a new file
		[[ "$(ls -f out/crashes)" != "" ]];

		RES="$?"
	fi


	if [[ "$RES" == 1 ]]; then
		RES=0
	elif [[ "$RES"==0 ]]; then
		RES=1
	fi

	cp stdout ..
	cd ..
	write_csv "$RES"

	set -e
}


# Write result in csv file. Reads outcome from "$WORKDIR""/stdout" file
write_csv() {
	# Get result from previous command
	local RES="$1"

	# Verify if RES is empty
	if [[ -z "$RES" ]]; then
		echo "Error3. Variable "$RES" is empty."
		touch err3
	fi	

	# Convert result to binary value
	if [[ "$RES" != 1 && "$RES" != "" && "$RES" != " " ]]; then
		RES=0
	fi

	# Get and save employed time
	T="$(grep "real" "$WORKDIR"/stdout)"
	if [[ "$?" == 1 ]]; then
		echo "Error. Time measurement has not been saved." 
		echo $T
		touch err
	fi	

	T2="$(echo "$T" | awk '{print $2}' | tr -d '\n')" 
	if [[ "$T2" == "" || "$T2" == " " ]]; then	
		echo "Error2. Time measurement has not been saved." 
		touch err2
	fi	

	echo -n "$T2" >> "$CSV_FILE"

	if [[ "$T2" == "file" ]]; then
		echo "$T1" > stderr.txt
	fi

	# Write result to csv output file
	if [[ "$OUT_FORMAT" == "multiline" ]]; then
		echo "" >>  "$CSV_FILE"
		echo "Result: "$RES" " >>  "$CSV_FILE"
	else
		echo -n " ""$RES"  >>  "$CSV_FILE"
	fi


	# Write framework name to csv output file
	if [[ "$OUT_FORMAT" == "multiline" ]]; then
		echo "" >>  "$CSV_FILE"
		echo "Framework: "$FRAMEWORK" " >>  "$CSV_FILE"
	else
		echo -n " ""$FRAMEWORK"  >>  "$CSV_FILE"
	fi
}


# Calculate number of arguments
select_arg_num() {

	n_args="$(wc -l "$LIST"_final | awk '{print $1}' | tr -d " ")"
}


# Save generated PUT to file in PUT_FOLDER
save_put() {
	output="$(printf '%s\n' "$PUT_FOLDER"/put_*.c)"

	if [[ "$output" == "$PUT_FOLDER""/put_*.c" ]]; then
		n_puts=0;
	else
		n_puts="$(echo "$output" | wc -l)"
	fi
	if [[ "$DEBUG" == "1" ]]; then
		echo "Number of PUTs in PUT folder ""$PUT_FOLDER"" (n_put):" "$n_puts"
	fi
	((n_puts=n_puts+1)) 
	
	if [[ ! -d "$PUT_FOLDER" ]]; then
		mkdir "$PUT_FOLDER"
	fi
	cp "$C_FILE2" "$PUT_FOLDER"/put_"$n_puts".c
}


# Save triggering input to file
save_input() {
	if [[ "$n_puts" == "" ]]; then
		n_puts=0;
	fi
	echo "$INPUT" > "$PUT_FOLDER"/"put_""$n_puts"_input	
}


# Save tranformation to file
save_trasf() {
	echo "$transformation" > "$PUT_FOLDER"/"put_""$n_puts"_trasf
}


read_from_file() {
	C_FILE2="$ARG"
	IN_FILE="${C_FILE2%.c}"_input

	INPUT="$(cat "$IN_FILE")"

	if [[ "$DEBUG" == "1" ]]; then
		echo "Processing file: ""$C_FILE2"" ..."
		
	fi	

	# get number of transformations
	c=""
	if [[ "$c" == "" ]]; then
	
		MATCH="$(echo "$C_FILE2" | egrep -o "(one|two|seven|ten)")"
		case "$MATCH" in

			one) c=1
				;;
			two) c=2
				;;
			seven) c=7
				;;
			ten) c=10
				;;
			*) c=-1; echo "Error. Cannot get number of transformations..."; touch err9
				;;
		esac
	fi
}




### Main program ###

set -e

if [[ "$2" == "" ]]; then
	echo ""
	echo "$0 <testing framework> <timeout (seconds)> <folder to save PUT into> <bug to inject> [optional file path]"
	echo ""
	echo "Supported testing frameworks: cbmc, klee, afl"
	echo ""
	echo "Supported bugs to inject:"
	echo ""
	echo "-ABORT_BUG (abort the program when the bug is reached)"
        echo "-ASSERT_BUG (cause an assertion violation when the error is reached)"
	echo ""
	exit 1
fi



cp "$C_FILE" "$C_FILE2"


update_csv


ARG="$5"

# if the program is called with empty cmdline argument ARG, read PUTs from file
if [[ "$ARG" != ""  ]]; then
	set +e
	read_from_file

	echo -e "\n==Testing input..."
	test_input
	if [[ "$FRAMEWORK" != "" ]]; then
		echo -e "\n==Testing selected framework..."
		test_"$FRAMEWORK"
	fi
else 
	select_arg_num
	echo -e "\n==Applying transformations..."
	apply_transformations
	echo -e "\n==Applying compiler transformations..."
	apply_compiler_transformations

	# Collect coverage information. Requires save_cov()
	# calculate_cov

	if [[ "$PUT_FOLDER" != "" ]]; then
		save_put
	fi
	echo -e "\n==Generating input..."
	set +e
	get_input 
	if [[ "$PUT_FOLDER" != "" ]]; then
		save_input
		save_trasf
	fi
	echo -e "\n==Testing input..."
	test_input

	# Perform differential testing with multiple compilers
	# test_input_multiple_compilers

	# Save and process collected coverage information. Requires calculate_cov()
	# save_cov 	

	if [[ "$FRAMEWORK" != "" ]]; then
		echo -e "\n==Testing selected framework..."
		test_"$FRAMEWORK"
	fi
	set -e
fi

exit 0
