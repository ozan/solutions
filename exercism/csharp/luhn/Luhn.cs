using System;
using System.Collections.Generic;
using System.Linq;

public class Luhn
{
    public long CheckDigit;
    public IEnumerable<int> Addends;
    public int Checksum;
    public bool Valid;

    public Luhn (long given)
    {
        CheckDigit = given % 10;
        Addends = given.ToString()
            .Reverse()
            .Select((ch, i) => i % 2 == 0 ? (ch - '0') : Wrap(ch))
            .Reverse();
        Checksum = Addends.Sum();
        Valid = Checksum % 10 == 0;
    }

    public static long Create (long given)
    {
        var candidate = given * 10;
        var l = new Luhn(candidate);
        if (l.Valid) return candidate;
        return candidate + 10 - l.Checksum % 10;
    }

    private int Wrap (char ch)
    {
        var n = (ch - '0') * 2;
        return n > 9 ? n - 9 : n;
    }

}
