using System;
using System.Collections.Generic;
using System.Linq;

public class Acronym
{
    public static string Abbreviate (string phrase)
    {
        var acronym = new List<char>();
        for (var i = 0; i < phrase.Length; i++) {
            var ch = phrase[i];
            var prior = i == 0 ? ' ' : phrase[i - 1];
            if (prior == ' ' ||
                prior == '-' ||
                Char.IsLower(prior) && Char.IsUpper(ch))
            {
                acronym.Add(Char.ToUpper(ch));
            }
        }
        return String.Concat(acronym);
    }

}
