using System;
using System.Collections.Generic;
using System.Linq;

public class PrimeFactors
{
    public static IEnumerable<int> For (long n, int k = 2)
    {
        if (n <= 1) return new int[0];
        for (; k <= n; k++) if (n % k == 0) break;
        return new List<int> { k }.Concat(PrimeFactors.For(n / k, k));
    }
}
