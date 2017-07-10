public class LargestSeriesProductCalculator {

    private final byte[] digits;

    LargestSeriesProductCalculator(String str) {
        if (str == null)
            throw new IllegalArgumentException("String to search must be non-null.");

        digits = new byte[str.length()];
        for (int i = 0; i < digits.length; i++) {
            char c = str.charAt(i);
            if (c < '0' || c > '9')
                throw new IllegalArgumentException("String to search may only contains digits.");
            digits[i] = (byte)(c - '0');
        }
    }

    long calculateLargestProductForSeriesLength(int n) {
        if (n > digits.length)
            throw new IllegalArgumentException("Series length must be less than or equal to the length of the string to search.");
        if (n < 0)
            throw new IllegalArgumentException("Series length must be non-negative.");
        if (n == 0) return 1;

        long prod = 1, max = 0;
        byte[] priors = new byte[n];
        for (int i = 0, m = 0; i < digits.length; i++) {
            byte d = digits[i];
            if (d == 0) {
                m = 0;
                prod = 1;
            } else {
                prod *= d;
                m += 1;
                if (m > n) prod /= priors[i % n];
                priors[i % n] = d;
                if (m >= n && prod > max) max = prod;
            }
        }
        return max;
    }
}
