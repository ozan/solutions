class SumOfMultiples {
    /*
    Determine the sum of multiples of _any_ member of `set` less than `number`.

    Uses the inclusion-exclusion principle as well as the formula for sum of an
    arithemetic series.

    If a, b and c are in `set`, then the sum of multiples of _any_ of these
    numbers is equal to:

        All multiples of a, plus multiples of b, plus multiples of c
        MINUS (multiples of both a and b, plus
               multiples of both b and c, plus
               multiples of both c and a)
        PLUS (multiples of a and b and c)

    ... etc. Now the multiples of a and b are the multiples of the least common
    multiple of a and b.

    We also know that lcm(a, b, c) = lcm(a, lcm(a, b))

    and that lcm(a, b) = a * b / gcd(a, b).

    Finally, the sum of multiples of a that are <= n is going to be

        a * m * (m + 1) / 2

    where m = floor(n / a) since e.g.:

        3 + 6 + 9 + 12 + 15 = 3 * (1 + 2 + 3 + 4 + 5)

    */

    private final int number;
    private final int[] set;

    SumOfMultiples(int number, int[] set) {
        this.number = number;
        this.set = set;
    }

    int gcd(int a, int b) {
        if (b > a) return gcd(b, a);
        if (b == 0) return a;
        return gcd(b, a % b);
    }

    int lcm(int a, int b) {
        return a * b / gcd(a, b);
    }

    int getSum() {
        int sum = 0;
        KCombinations kc = new KCombinations(set);
        int[][] combos;
        for (int k = 1, sign = 1; k <= set.length; k++, sign *= -1) {
            combos = kc.combinations(k);
            for (int ci = 0; ci < combos.length; ci++) {
                int lcm = 1;
                for (int cj = 0; cj < k; cj++)
                    lcm = this.lcm(lcm, combos[ci][cj]);
                int n = (number - 1) / lcm;
                sum += sign * lcm * n * (n + 1) / 2;
            }
        }
        return sum;
    }
}
