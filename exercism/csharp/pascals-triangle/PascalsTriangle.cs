using System;
using System.Collections.Generic;
using System.Linq;

public class PascalsTriangle
{
    public static IEnumerable<IEnumerable<int>> Calculate (int n)
    {
        IEnumerable<int> row = new[] { 1 };
        while (n > 0) {
            yield return row;
            row = NextRow(row);
            n--;
        }
    }

    static IEnumerable<int> NextRow (IEnumerable<int> previous)
    {
        var xs = previous.Concat(new[] { 0 });
        var ys = new[] { 0 }.Concat(previous);
        return xs.Zip(ys, (x, y) => x + y);
    }
}
