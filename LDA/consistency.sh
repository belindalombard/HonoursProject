#!/bin/sh
start=$(date +%s.%N)

echo '' > con.txt
echo '' > results_consistency.txt
echo '' > results_metadata.txt


if [ $# -eq 0 ]
then
	for T in 5 10 15 20 
	do
		for P in 3 5 7 10 
		do
			python3 2_lda.py $T 1 $P
		done
	done
else 
	python3 2_lda.py 10 1 5
fi

duration=$(echo "$(date +%s.%N) - $start" | bc)

echo "Duration: $duration"

