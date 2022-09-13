#================================================================================================
#
#  FILE:
#	list_to_func.awk
#
#  DESCRIPTION:
# 	Transform list of transformations to list of functions. 
#
#  USAGE:
#	awk -f list_to_func.awk	<list_of_transformations_file>
#
#================================================================================================



BEGIN {
	# INPUT PARAMETERS
	#
	# 0=parameters from file (default) 1=random parameters
	# rand_param=0
	#
	# Final transformation to apply. Valid values: ASSERT_BUG, ABORT_BUG
	# final_transformation="ABORT_BUG" #"ASSERT BUG"
	


	# INTERNAL PARAMETERS

	# initial transformation
	initial_transformation="INIT("

	# transformation string
	transformation=""

	# line number
	ln=1

	# initial seed for prng
	srand(seed)
}


{
	# transformation name
	transformation=transformation toupper($1)"("

	# transformation input sources
	transformation=transformation $2","

	# transformation parameters
	if (rand_param) {
		for (i=3;i<=NF;i++) {transformation= transformation int(rand()*$i)","}

	} else {
		for (i=3;i<=NF;i++) {transformation= transformation $i","}
	}

	# transformation number (for variable renaming)	
	transformation= transformation ln","  

	# increment line number
	ln=ln+1

}


END {
	printf initial_transformation
	printf ln-1","
	printf transformation

	# final transformation
	printf final_transformation

	# final parenthesis		
	for (i=0;i<ln;i++) {printf ")"}
}
