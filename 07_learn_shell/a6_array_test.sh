#!/bin/bash

array=(1 2 3 4 5)

echo $array

array[2]=100

echo ${array[2]}
echo ${array[@]}

:<<!
a
b
c
d
e
f
g
!

length=${#array[@]}
echo $length
length=${#array[2]}
echo $length
