class NaturalNumber {

    private final int n;

    NaturalNumber(int n) {
        if (n <= 0) throw new IllegalArgumentException("You must supply a natural number (positive integer)");
        this.n = n;
    }

    Classification getClassification() {
        int total = 0;
        for (int i = 1; i < this.n; i++)
            if (n % i == 0) total += i;

        if (total == n) return Classification.PERFECT;
        if (total < n) return Classification.DEFICIENT;
        return Classification.ABUNDANT;
    }

}
