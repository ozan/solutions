using System;
using System.Collections.Generic;
using System.Linq;

public class Sieve
{
    public static IEnumerable<int> Primes (int upto)
    {
        var candidates = Enumerable.Range(0, upto + 1).ToArray();
        var p = 2;
        yield return p;
        while (p < upto) {
            // null out divisors
            for (var q = 2; q < (double)upto / p; q++) {
                candidates[p * q] = 0;
            }
            // increase p to next known prime
            if (p > 2) yield return p;
            p++;
            while (candidates[p] == 0) p++;
        }
    }
}
