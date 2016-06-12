using System;
using System.Collections.Generic;
using System.Linq;

public class Triplet
{
    int A;
    int B;
    int C;

    public Triplet (int a, int b, int c)
    {
        A = a;
        B = b;
        C = c;
    }

    public int Sum ()
    {
        return A + B + C;
    }

    public int Product ()
    {
        return A * B * C;
    }

    public bool IsPythagorean ()
    {
        return A * A + B * B == C * C;
    }

    public static IEnumerable<Triplet> Where (int maxFactor, int minFactor=1)
    {
        for (int a = minFactor; a <= maxFactor; a++) {
            for (int b = a + 1; b <= maxFactor; b++) {
                var c = Math.Sqrt(a * a + b * b);
                if ((int)c == c && c <= maxFactor) {
                    yield return new Triplet(a, b, (int)c);
                }
            }
        }
    }

    public static IEnumerable<Triplet> Where (int sum, int maxFactor, int minFactor=1)
    {
        foreach (Triplet t in Where(maxFactor: maxFactor, minFactor: minFactor)) {
            if (t.Sum() == sum) yield return t;
        }
    }
}
