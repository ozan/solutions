using System;
using System.Collections.Generic;
using System.Linq;

namespace Exercism
{
    public static class Phrase
    {
        public static Dictionary<string, int> WordCount(string phrase)
        {
            var tokens = Tokenize(phrase);
            var counts = new Dictionary<string, int>();
            foreach (var token in tokens) {
                if (counts.ContainsKey(token)) {
                    counts[token] = counts[token] + 1;
                } else {
                    counts.Add(token, 1);
                }
            }
            return counts;
        }

        private static List<string> Tokenize(string phrase)
        {
            var tokens = new List<string>();
            var currentWord = new List<char>();

            foreach (var ch in (phrase + " ")) {
                // allow appostrophes within words, but not at start or end
                if (Char.IsLetter(ch)
                      || Char.IsDigit(ch)
                      || ch == '\'' && currentWord.Count > 0) {
                    currentWord.Add(ch);
                } else if (currentWord.Count > 0) {
                    if (currentWord.Last() == '\'') currentWord.RemoveAt(currentWord.Count - 1);
                    tokens.Add(String.Concat(currentWord).ToLower());
                    currentWord.Clear();
                }
            }

            return tokens;
        }
    }
}
