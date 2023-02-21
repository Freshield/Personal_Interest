#!/usr/bin/env bash

demoFun(){
    echo "It is the first shell func"
}

demoFun

funWithReturn(){
    echo "This func will add two values"
    echo "input first num"
    read aNum
    echo "input second num"
    read anotherNum
    echo "two values are $aNum and $anotherNum !"
    return $(($aNum+$anotherNum))
}

funWithReturn
echo "The res is $?"