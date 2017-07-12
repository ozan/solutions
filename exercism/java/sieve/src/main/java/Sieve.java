import java.util.*;

public class Sieve {
    private final int n;

    Sieve(int n) {
        this.n = n;
    }

    List<Integer> getPrimes() {
        ArrayList<Integer> primes = new ArrayList<Integer>();
        byte[] sieve = new byte[n + 1];
        for (int p = 2; p <= n; p++) {
            if (sieve[p] == 1) continue;
            primes.add(p);
            for (int q = p; q <= n; q += p)
                sieve[q] = 1;
        }
        return primes;
    }
}
