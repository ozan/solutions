using System;
using System.Collections.Generic;
using System.Linq;

public class Complement
{
    private static Dictionary<char, char> Table = new Dictionary<char, char> {
        { 'G', 'C' },
        { 'C', 'G' },
        { 'T', 'A' },
        { 'A', 'U' }
    };

    public static IEnumerable<char> OfDna (string dna)
    {
        return dna.Select(ch => Table[ch]);
    }
}
