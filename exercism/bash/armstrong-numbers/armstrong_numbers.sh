#!/bin/bash

# Iterate through digits and accumulate the total
digits=$1
n=${#digits}
total=0
while read -r -n1 digit; do
    ((total += digit ** n))
done <<< "$digits"

# Print and return the result 
[[ $total -eq $digits ]] && echo 'true' && exit 0
echo 'false' && exit 1

