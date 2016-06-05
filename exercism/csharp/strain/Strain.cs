using System;
using System.Collections.Generic;

public static class EnumerableExtensions
{
    public static IEnumerable<T> Keep<T> (this IEnumerable<T> source, Func<T, bool> f)
    {
        foreach (var item in source) if (f(item)) yield return item;
    }

    public static IEnumerable<T> Discard<T> (this IEnumerable<T> source, Func<T, bool> f)
    {
        return source.Keep(x => !f(x));
    }
}
