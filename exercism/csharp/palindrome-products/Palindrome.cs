using System;
using System.Collections.Generic;
using System.Linq;


public class Palindrome
{
    public int Value;
    public List<Tuple<int, int>> Factors;

    public Palindrome (int val, List<Tuple<int, int>> factors)
    {
        Value = val;
        Factors = factors;
    }

    public static Palindrome Smallest (int max)
    {
        return Smallest(1, max);
    }

    public static Palindrome Smallest (int min, int max)
    {
        return FirstMatching(Palindromes(), min, max);
    }

    public static Palindrome Largest (int max)
    {
        return Largest(1, max);
    }

    public static Palindrome Largest (int min, int max)
    {
        int fromLength = (int)Math.Ceiling(Math.Log10(max * max));
        var candidates = Palindromes(fromLength, -1);
        return FirstMatching(candidates, min, max);
    }

    static Palindrome FirstMatching (IEnumerable<string> palindromes, int min, int max)
    {
        var candidates = palindromes.Select(n => int.Parse(n)).Where(n => n >= min * min);
        foreach (var val in candidates) {
            var factors = FactorsOf(val, min, max).ToList();
            if (factors.Any()) {
                return new Palindrome(val, factors);
            }
        }
        throw new ArgumentException("No palindrome products in range");
    }

    static IEnumerable<string> Palindromes (int fromLength = 1, int direction = 1)
    {
        int length = fromLength;
        while (true) {
            foreach (string p in PalindromesOfLength(length, direction)) {
                if (p[0] != '0') yield return p;
            }
            length += direction;
        }

    }

    static IEnumerable<string> PalindromesOfLength (int n, int direction) {
        if (n == 0) yield return "";
        if (n == 1) {
            var range = Enumerable.Range(1, 9).Select(d => d.ToString());
            range = direction == 1 ? range : range.Reverse();
            foreach (var d in range) {
                yield return d;
            }
        }
        if (n > 1) {
            var range = Enumerable.Range(0, 10).Select(d => d.ToString());
            range = direction == 1 ? range : range.Reverse();
            foreach (var wrap in range) {
                var inner = PalindromesOfLength(n - 2, direction);
                foreach (var p in inner.Select(d => wrap + d + wrap)) {
                    yield return p;
                }
            }
        }
    }

    static IEnumerable<Tuple<int, int>> FactorsOf (int val, int min, int max)
    {
        var iterMax = Math.Min(max, Math.Floor(Math.Sqrt(val)));
        for (var d = min; d <= iterMax; d++) {
            var q = val / d;
            if (val % d == 0 && q >= min && q <= max) {
                yield return Tuple.Create(d, val / d);
            }
        }
    }
}
