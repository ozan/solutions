using System;
using System.Collections.Generic;
using System.Linq;

public class OcrNumbers
{

    static string[] Signatures = SplitDigits(
      " _     _  _     _  _  _  _  _ " + "\n" +
      "| |  | _| _||_||_ |_   ||_||_|" + "\n" +
      "|_|  ||_  _|  | _||_|  ||_| _|" + "\n" +
      "                              "
    );

    public static string Convert (string pic)
    {
        return String.Concat(SplitDigits(pic).Select(Number));
    }

    static string[] SplitDigits (string pic)
    {
        return Chunk(3, Transpose(pic.Split('\n')))
            .Select(Transpose)
            .Select(dig => String.Join("\n", dig.Select(line => String.Concat(line))))
            .ToArray();
    }

    static char Number (string signature)
    {
        var idx = Array.IndexOf(Signatures, signature);
        return idx > -1 ? idx.ToString()[0] : '?';
    }

    static IEnumerable<IEnumerable<T>> Transpose<T> (IEnumerable<IEnumerable<T>> matrix)
    {
        return matrix.First().Select((_, i) => matrix.Select(row => row.Skip(i).First()));
    }

    static IEnumerable<IEnumerable<T>> Chunk<T> (int n, IEnumerable<T> xs)
    {
        while (xs.Any()) {
            yield return xs.Take(n);
            xs = xs.Skip(n);
        }
    }
}
