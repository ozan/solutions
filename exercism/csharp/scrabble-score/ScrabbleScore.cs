using System.Collections.Generic;
using System.Linq;

namespace Exercism
{
    public static class Scrabble
    {
        public static int Score(string word)
        {
            if (word == null) return 0;
            return word.ToUpper().Select(letterScore).Aggregate(0, (a, b) => a + b);
        }

        private static int letterScore(char ch)
        {
            var scores = new Dictionary<char, int>{
                {'A', 1}, {'E', 1}, {'I', 1}, {'O', 1}, {'U', 1}, {'L', 1}, {'N', 1}, {'R', 1}, {'S', 1}, {'T', 1},
                {'D', 2}, {'G', 2},
                {'B', 3}, {'C', 3}, {'M', 3}, {'P', 3},
                {'F', 4}, {'H', 4}, {'V', 4}, {'W', 4}, {'Y', 4},
                {'K', 5},
                {'J', 8}, {'X', 8},
                {'Q', 10}, {'Z', 10},
            };
            return scores.ContainsKey(ch) ? scores[ch] : 0;
        }
    }
}
