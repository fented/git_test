#!/bin/bash
echo "running $0"

if [ -z ${1+x} ];
    then echo "Incorrect Usage (./listdirTest directory/to/list/"
        else
    echo "Getting content of $1:"
    echo ""
    ls $1
fi