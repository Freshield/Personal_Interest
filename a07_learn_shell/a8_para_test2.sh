#!/bin/bash

echo "-- \$* showing --"
for i in "$*"; do
    echo $i
done

echo "-- \$@ showing --"
for i in "$@"; do
    echo $i
done