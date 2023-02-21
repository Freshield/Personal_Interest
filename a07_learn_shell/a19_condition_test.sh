#!/usr/bin/env bash

if [ $(ps -ef | grep -c "ssh") -gt 1 ]; then echo "true";fi

a=10
b=20
if [ $a == $b ]
then
    echo "a eq b"
elif [ $a -gt $b ]
then
    echo "a greater b"
elif [ $a -lt $b ]
then
    echo "a less b"
else
    echo "error"
fi

for loop in 1 2 3 4 5
do
    echo "The value is: $loop"
done

int=1
while (($int<=5)); do
    echo $int
    let "int++"
done