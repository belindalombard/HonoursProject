#!/bin/sh


#Script used to estimate the minimum number of runs needed
echo '' > numruns.txt

for i in 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40
do
	python3 2_lda.py $i 0 >> numruns.txt
done

