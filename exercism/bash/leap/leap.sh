if [[ $# -ne 1 ]] || ! [[ $1 =~ ^[0-9]+$ ]]; then
    echo 'Usage: leap.sh <year>'
    exit 1
fi

n=$1
if ((n % 400 == 0 || n % 100 != 0 && n % 4 == 0)); then
    echo 'true'
else
    echo 'false'
fi

