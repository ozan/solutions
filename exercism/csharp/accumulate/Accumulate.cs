using System;
using System.Collections.Generic;

public static class EnumerableExtensions
{
    public static IEnumerable<T> Accumulate<T> (this IEnumerable<T> source, Func<T, T> f)
    {
        foreach (var item in source)
        {
            yield return f(item);
        }
    }
}
