A=0;C=0;G=0;T=0
for ((i=0; i < ${#1}; i++)); do
    case ${1:i:1} in
        A) ((A += 1));;
        C) ((C += 1));;
        G) ((G += 1));;
        T) ((T += 1));;
        *) echo 'Invalid nucleotide in strand'; exit 1;;
    esac
done

printf 'A: %d\nC: %d\nG: %d\nT: %d\n' $A $C $G $T
