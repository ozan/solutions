using System;
using System.Collections.Generic;
using System.Linq;

public class PigLatin
{
    static string[] ConstStems = new string[] { "ch", "qu", "squ", "thr", "th", "sch" };
    static string[] VowelStems = new string[] { "yt", "xr", "a", "e", "i", "o", "u" };

    public static string Translate (string given)
    {
        return String.Join(" ", given.Split().Select(TranslateWord));
    }

    static string TranslateWord (string word)
    {
        string head, tail;
        foreach (var stem in ConstStems)
        {
            head = word.Substring(0, stem.Length);
            tail = word.Substring(stem.Length);
            if (head == stem) return tail + head + "ay";
        }
        foreach (var stem in VowelStems)
        {
            head = word.Substring(0, stem.Length);
            tail = word.Substring(stem.Length);
            if (head == stem) return head + tail + "ay";
        }
        return word.Substring(1) + word[0] + "ay";
    }
}
