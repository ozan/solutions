scores=(0 1 3 3 2 1 4 2 4 1 8 5 1 3 1 1 3 10 1 1 1 1 4 4 8 4 10)
total=0
for ((i=0; i < ${#1}; i++)); do
    ord=$(printf '%d' "'${1:i:1}")  # get ordinal value of ASCII character
    si=$((ord &= 0x1f))  # use inherent structure of ASCII table to handle case
    ((total += ${scores[si]}))
done
echo $total

