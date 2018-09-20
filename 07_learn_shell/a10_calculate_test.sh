#!/usr/bin/env bash

val=`expr 2 + 2`
echo "res is ${val}"

a=10
b=20

val=`expr $a + $b`
echo "1 ${val}"

val=`expr $a - $b`
echo "2 ${val}"

val=`expr $a \* $b`
echo "3 ${val}"

val=`expr $b / $a`
echo "4 ${val}"

val=`expr $b % $a`
echo "5 ${val}"

if [ $a == $b ]
then
    echo "a equal b"
fi

if [ $a != $b ]
then
    echo "a not equal b"
fi