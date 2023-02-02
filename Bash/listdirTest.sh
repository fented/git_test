#!/bin/bash
echo "running $0"
echo ""
if [ -z ${1+x} ];
    then echo "Incorrect Usage (./listdirTest directory/to/list/"
        else
    echo "cd \$1"
    cd $1
    echo "pwd:"
    pwd
    echo ""
    echo "ls \$1:"
    ls $1
fi