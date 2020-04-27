
int scratch(int num) {
    if (num % 4 != 0) return 0;
    // now, must be divisible by 4
    if (num % 100 != 0) return 1;
    // now, must be divisible by 4 but not 100
    return num % 400 == 0;
}
