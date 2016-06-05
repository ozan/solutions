using System;
using System.Collections.Generic;
using System.Linq;

public class Trinary
{
    public static int ToDecimal (string digits)
    {
        if (digits.Except("012").Any()) return 0;
        return digits
          .Reverse()
          .Select((ch, i) => (int)Math.Pow(3, i) * (ch - '0'))
          .Sum();
    }
}
