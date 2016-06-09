using System;
using System.Collections.Generic;
using System.Linq;

public class Hexadecimal
{
    static string Hex = "0123456789abcdef";

    public static int ToDecimal(string digits)
    {
        IEnumerable<int> vals =
            digits
            .Reverse()
            .Select((d, i) => (int)Math.Pow(16, i) * Hex.IndexOf(d));
        if (vals.Where(n => n == -1).Any()) return 0;
        return vals.Sum();
    }
}
