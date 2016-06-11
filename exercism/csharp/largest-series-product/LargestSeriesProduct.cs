using System;
using System.Collections.Generic;
using System.Linq;

public class LargestSeriesProduct
{
    IEnumerable<int> Digits;

    public LargestSeriesProduct (string digitString)
    {
        Digits = digitString.Select(ch => ch - '0');
    }

    public int GetLargestProduct (int n)
    {
        if (n == 0) return 1;
        if (n > Digits.Count()) throw new ArgumentException();
        
        int max = 0;
        for (var i = 0; i < Digits.Count() - n + 1; i++)
        {
            int prod = Digits.Skip(i).Take(n).Aggregate((a, b) => a * b);
            if (prod > max) max = prod;
        }
        return max;
    }
}
