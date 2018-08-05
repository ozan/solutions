case "$1" in
    total) printf '%u' $((0xffffffffffffffff));;
    [1-9]|[1-5][0-9]|6[0-4]) printf '%u' $((1 << $1 - 1));;
    *) printf 'Error: invalid input'; exit 1;;
esac
