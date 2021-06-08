#! /bin/bash

if python ./student_py/*.py < inputs.txt 
then
    echo
    echo Program run successfully: 2/2
else
    echo
    echo UNSUCCESSFUL: 0/2
fi

echo

python check.py

echo "Delete student answer? (y/n)" 
read -r choice

if [ "$choice" = "y" ]
then
    rm student_py/*.py
fi
