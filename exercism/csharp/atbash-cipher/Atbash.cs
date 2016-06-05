using System;
using System.Collections.Generic;
using System.Linq;

public class Atbash
{
    public static string Encode (string given)
    {
        var converted = given
          .ToLower()
          .Where(Char.IsLetterOrDigit)
          .Select(EncodeChar);
        return String.Join(" ", Chunk(5, converted));
    }

    private static char EncodeChar (char ch)
    {
        return Char.IsDigit(ch) ? ch : (char)('a' + 'z' - ch);
    }

    private static IEnumerable<String> Chunk (int size, IEnumerable<char> source)
    {
        while (source.Any())
        {
            yield return String.Concat(source.Take(size));
            source = source.Skip(size);
        }
    }
}
