using NUnit.Framework;

using Exercism;

[TestFixture]
public class RomanNumeralsTest
{

    [Test]
    public void Convert_roman_to_arabic_numerals()
    {
        var cases = new [] {
          new { arabic = 0, roman =  "" },
          new { arabic = 1, roman =  "I" },
          new { arabic = 2, roman =  "II" },
          new { arabic = 3, roman =  "III" },
          new { arabic = 4, roman =  "IV" },
          new { arabic = 5, roman =  "V" },
          new { arabic = 6, roman =  "VI" },
          new { arabic = 9, roman =  "IX" },
          new { arabic = 27, roman =  "XXVII" },
          new { arabic = 48, roman =  "XLVIII" },
          new { arabic = 59, roman =  "LIX" },
          new { arabic = 93, roman =  "XCIII" },
          new { arabic = 141, roman =  "CXLI" },
          new { arabic = 163, roman =  "CLXIII" },
          new { arabic = 402, roman =  "CDII" },
          new { arabic = 575, roman =  "DLXXV" },
          new { arabic = 911, roman =  "CMXI" },
          new { arabic = 1024, roman =  "MXXIV" },
          new { arabic = 3000, roman =  "MMM" }
        };

        foreach (var tc in cases) {
            Assert.That(RomanNumeral.FromArabic(tc.arabic), Is.EqualTo(tc.roman));
        }
    }
}
