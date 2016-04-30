using System;
using System.Collections.Generic;


namespace Exercism
{
    public class DNA
    {
        public Dictionary<char, int> NucleotideCounts = new Dictionary<char, int>
        {
            { 'A', 0 },
            { 'G', 0 },
            { 'C', 0 },
            { 'T', 0 }
        };

        public DNA(string nucleotides)
        {
            foreach (var ch in nucleotides) NucleotideCounts[ch] += 1;
        }

        public int Count(char ch)
        {
            if (!NucleotideCounts.ContainsKey(ch)) throw new InvalidNucleotideException();
            return NucleotideCounts[ch];
        }
    }

    public class InvalidNucleotideException : Exception
    {
        public InvalidNucleotideException()
        {
        }
    }
}
