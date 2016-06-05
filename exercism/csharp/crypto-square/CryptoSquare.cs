using System;
using System.Collections.Generic;
using System.Linq;

public class Crypto
{
    public string NormalizePlaintext;
    public int Size;

    public Crypto (string given)
    {
        NormalizePlaintext = String.Concat(given.Where(Char.IsLetterOrDigit)).ToLower();
        Size = (int)Math.Ceiling(Math.Sqrt(NormalizePlaintext.Length));
    }

    public IEnumerable<IEnumerable<char>> PlaintextSegments ()
    {
        IEnumerable<char> text = NormalizePlaintext;
        while (text.Any())
        {
            yield return text.Take(Size);
            text = text.Skip(Size);
        }
    }

    public string Ciphertext ()
    {
        var segments = PlaintextSegments();
        return String.Concat(Transposed(segments));
    }

    public string NormalizeCiphertext ()
    {
        var segments = PlaintextSegments();
        return String.Join(" ", Transposed(segments));
    }

    private IEnumerable<string> Transposed (IEnumerable<IEnumerable<char>> segments)
    {
        foreach (var i in Enumerable.Range(0, Size))
        {
            var s = segments
                .Select(xs => xs.ElementAtOrDefault(i))
                .Where(ch => ch != '\0');
            yield return String.Concat(s);
        }
    }
}
