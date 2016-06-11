using System;
using System.Collections.Generic;
using System.Linq;

public class NthPrime
{
    public static int Nth (int n)
    {
        var primes = new HashSet<int>();
        var p = 2;
        while (true) {
            var isPrime = true;
            foreach (var q in primes) {
                if (p % q == 0) {
                    p++;
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                primes.Add(p);
                if (primes.Count() == n) return p;
                p++;
            }
        }
    }
}
