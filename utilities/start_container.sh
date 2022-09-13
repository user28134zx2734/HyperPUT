#!/bin/bash

#================================================================================================
#
#  FILE:
#	start_containers.sh
#
#  DESCRIPTION:
# 	Start KLEE container and copy necessary files. 
#
#  USAGE:
#	chmod u+x start_containers.sh
#	./start_containers.sh
#
#
#================================================================================================


USER="user"
WORKDIR=/home/$USER/Desktop/PUT_generator_v0.407

ID="$(docker run -d --rm -ti --ulimit='stack=-1:-1' klee/klee)" 

if [[ "$?" != 0 ]]; then
	echo "Error in starting container. Exitings..."
	exit -1	
fi

# Copy the entire workdir in the container
# docker cp "$WORKDIR" $ID:/home/klee

