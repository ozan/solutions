using System;
using System.Collections.Generic;
using System.Linq;

public class WordProblem
{
    static Dictionary<string, Func<int, int, int>> Ops = new Dictionary<string, Func<int, int, int>> {
        { "plus", (a, b) => a + b },
        { "minus", (a, b) => a - b },
        { "divided", (a, b) => a / b },
        { "multiplied", (a, b) => a * b }
    };

    public static int Solve(string phrase)
    {
        if (phrase[phrase.Length - 1] == '?') phrase = phrase.Substring(0, phrase.Length - 1);
        var words = phrase.Substring(8, phrase.Length - 8).Split(' ').Where(w => w != "by");
        int memo;
        try {
          memo = Int32.Parse(words.First());
        } catch (FormatException e) {
          throw new ArgumentException();
        }
        words = words.Skip(1);
        while (words.Any()) {
            Func<int, int, int> op;
            try {
                op = Ops[words.First()];
            } catch (KeyNotFoundException e) {
                throw new ArgumentException();
            }
            var operand = Int32.Parse(words.Skip(1).First());
            memo = op(memo, operand);
            words = words.Skip(2);
        }
        return memo;
    }
}
