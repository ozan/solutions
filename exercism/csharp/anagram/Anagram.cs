using System;
using System.Collections.Generic;
using System.Linq;

namespace Exercism
{
    public class Anagram
    {
        string original;

        public Anagram(string original)
        {
            this.original = original.ToLower();
        }

        public IEnumerable<string> Match(IEnumerable<string> words)
        {
            return (from word in words
                    where Sorted(word.ToLower()) == Sorted(this.original)
                      && word.ToLower() != this.original
                    select word);
        }

        private string Sorted(string str)
        {
            return String.Concat(str.OrderBy(c => c));
        }
    }
}
