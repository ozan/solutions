using System;
using System.Collections.Generic;
using System.Linq;

namespace Exercism
{
    public class TwelveDaysSong
    {
        string [] gifts = {
            "a Partridge in a Pear Tree",
            "two Turtle Doves",
            "three French Hens",
            "four Calling Birds",
            "five Gold Rings",
            "six Geese-a-Laying",
            "seven Swans-a-Swimming",
            "eight Maids-a-Milking",
            "nine Ladies Dancing",
            "ten Lords-a-Leaping",
            "eleven Pipers Piping",
            "twelve Drummers Drumming"
        };

        string [] ordinals = {
            "first",
            "second",
            "third",
            "fourth",
            "fifth",
            "sixth",
            "seventh",
            "eighth",
            "ninth",
            "tenth",
            "eleventh",
            "twelfth"
        };

        public string Verse(int verse)
        {
            return prelude(verse) + humanJoin(gifts.Take(verse).Reverse()) + ".\n";
        }

        public string Verses(int start, int end)
        {
            return String.Join("\n", Enumerable.Range(start, end).Select(Verse)) + '\n';
        }

        public string Sing()
        {
            return Verses(1, 12);
        }

        private string prelude(int day) {
            return String.Format("On the {0} day of Christmas my true love gave to me, ", ordinals[day - 1]);
        }

        private string humanJoin(IEnumerable<string> phrases) {
            if (phrases.Count() == 1) return phrases.First();
            var allBut = phrases.Take(phrases.Count() - 1);
            var last = phrases.Last();
            return String.Concat(new string [] { String.Join(", ", allBut), ", and ", last });
        }
    }
}
