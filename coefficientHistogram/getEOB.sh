#!/bin/bash

#for i in seq '1 5000'; do

while read line; do 
	echo $line | grep "0:" | sed 's/ /,/g' | sed -e 's/[,0]*$//g' | cut -d : -f1 --complement | cut -d, -f1 --complement | sed 's/,/ /g' | wc -w

done < x.out

#done
