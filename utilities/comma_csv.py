#/usr/bin/python3

#================================================================================================
#
#  FILE:
#	comma_csv.py
#
#  DESCRIPTION:
#	Add commas to csv file and improve header for visualization.
#
#  USAGE:
#	chmod u+x comma_csv.py
#	./comma_csv.py
#
#================================================================================================


import sys
import os
import pandas as pan

# Work directory.
user="user"
WORKDIR="/home/" + user + "/Desktop/PUT_generator_v0.405/test_out/"

csv_files=[WORKDIR + str("comb1_7.csv"),WORKDIR + str("comb1_k_7.csv"),WORKDIR + str("comb2_7.csv"),WORKDIR + str("comb2_k_7.csv"),WORKDIR + str("comb5_7.csv"),WORKDIR + str("comb5_k_7.csv"),WORKDIR + str("comb7_7.csv"),WORKDIR + str("comb7_k_7.csv"),WORKDIR + str("comb10_7.csv"),WORKDIR + str("comb10_k_7.csv")]


for csv_file in csv_files:
    data=pan.read_csv(csv_file, sep=" ")

    # insert bf in header
    for col in data.columns:
        ncol="\\textbf{" + col + "}"
        data.rename(columns={col:ncol},inplace=True)

    #insert comma separator
    data.to_csv(csv_file + str("_comma.csv"), sep=",", index=False)

