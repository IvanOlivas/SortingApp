#!/usr/bin/env bash

#Test sort 1 - normal sorting alphabetically and then by length
python callSortAL.py < Sort_Me.txt > output1.txt

if diff output1.txt Sorted.txt; then
    echo "Sort A/L passes"
else
    echo "Sort A/L fails"
fi

#Test sort 2 - sorting alphabetically and then by length and then reversing
python callSortRev.py < Sort_Me.txt > output2.txt

if diff output2.txt SortedReversed.txt; then
    echo "Sort with reverse passes"
else
    echo "Sort with reverse fails"
fi
