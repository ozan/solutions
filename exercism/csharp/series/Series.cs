using System;
using System.Collections.Generic;
using System.Linq;

public class Series
{
    IEnumerable<int> Digits;

    public Series(string given)
    {
        Digits = given.Select(ch => ch - '0');
    }

    public List<int []> Slices(int n)
    {
        if (n > Digits.Count()) throw new ArgumentException();
        var q = new Queue<int>(n);
        var l = new List<int[]>();
        foreach (var d in Digits)
        {
            q.Enqueue(d);
            if (q.Count == n) {
              l.Add(q.ToArray());
              q.Dequeue();
            }
        }
        return l;
    }
}
