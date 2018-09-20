#!/usr/bin/env bash

num1=100
num2=100

if test $[num1] -eq $[num2]
then
    echo 'num1 eq num2'
else
    echo 'not eq'
fi

a=5
b=6
result=$[a+b]
echo "result is: $result"