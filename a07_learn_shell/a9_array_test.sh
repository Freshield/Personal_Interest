#!/bin/bash

my_array=(A B "C" D)

my_array[4]=E

echo ${my_array[@]}
echo ${my_array[*]}

echo "length is ${#my_array[@]}"