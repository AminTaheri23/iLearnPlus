#!/bin/bash

# This script is used to generate head of each csv file in the feature data and save it to head_files directory.

for file in `ls *.csv`
do
    head -n 10000 $file > head_files/$file
    # tail -n 1 $file >> head_files/$file
done