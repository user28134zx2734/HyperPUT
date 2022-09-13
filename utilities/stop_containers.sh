#!/bin/bash

#================================================================================================
#
#  FILE:
#	stop_containers.sh
#
#  DESCRIPTION:
# 	Stop running containers. 
#
#  USAGE:
#	chmod u+x stop_containers.sh
#	./stop_containers.sh
#
#================================================================================================


IDs="$(docker ps | awk '{if ($1 != "CONTAINER") print $1}')"

for id in $IDs; do
	docker stop $id

done

# Confirm that all containers have been stopped
echo -e "Running containers after script execution:\n\n"
docker ps
