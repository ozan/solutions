#!/bin/bash

[[ $# -ne 2 ]] && echo 'Usage: hamming.sh <strand1> <strand2>' && exit 1
[[ ${#1} -ne ${#2} ]] && echo 'left and right strands must be of equal length' && exit 1

count=0
while read -rn1 x <&3 && read -rn1 y <&4; do
    [[ "$x" != "$y" ]] && ((count++))
done 3<<<"$1" 4<<<"$2"

echo $count
