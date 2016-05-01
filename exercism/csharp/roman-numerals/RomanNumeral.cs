using System;
using System.Collections.Generic;


namespace Exercism
{
    public static class RomanNumeral
    {
        public static string FromArabic(int arabic)
        {
            return String.Concat(fromArabic(arabic, new List<string>()));
        }

        private static List<string> fromArabic(int arabic, List<string> roman)
        {
            if (arabic == 0) return roman;

            foreach (var item in arabicToRoman) {
                if (arabic >= item.arabic) {
                    roman.Add(item.roman);
                    return fromArabic(arabic - item.arabic, roman);
                }
            }

            throw new Exception("Is the smallest unit defined?");
        }

        private class AtoR {
            public int arabic;
            public string roman;
        }

        private static AtoR [] arabicToRoman = new AtoR [] {
            new AtoR { arabic = 1000, roman = "M" },
            new AtoR { arabic = 900, roman = "CM" },
            new AtoR { arabic = 500, roman = "D" },
            new AtoR { arabic = 400, roman = "CD" },
            new AtoR { arabic = 100, roman = "C" },
            new AtoR { arabic = 90, roman = "XC" },
            new AtoR { arabic = 50, roman = "L" },
            new AtoR { arabic = 49, roman = "IL" },
            new AtoR { arabic = 40, roman = "XL" },
            new AtoR { arabic = 10, roman = "X" },
            new AtoR { arabic = 9, roman = "IX" },
            new AtoR { arabic = 5, roman = "V" },
            new AtoR { arabic = 4, roman = "IV" },
            new AtoR { arabic = 1, roman = "I" }
        };
    }
}
