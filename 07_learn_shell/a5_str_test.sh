#!/bin/bash

str='this is a string''test'
echo $str

your_name='runoob'
str="Hello, I know you are \"$your_name\"! \n"
echo $str

greeting="hello, "$your_name" !"
greeting_1="hello, ${your_name} !"
echo $greeting $greeting_1

greeting_2='hello, '$your_name' !'
greeting_3='hello, ${your_name} !'
echo $greeting_2 $greeting_3

string="abcd"
echo ${#string}

string="runoob is a great site"
echo ${string:1:4}

echo `expr index "$string" io`

