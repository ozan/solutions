using System;
using System.Collections.Generic;
using System.Linq;

public class Octal
{
    public static int ToDecimal (string given)
    {
        // validate
        if (given.Where(ch => ch < '0' || ch > '7').Any()) return 0;
        return given.Reverse().Select((ch, i) => (int)Math.Pow(8, i) * (ch - '0')).Sum();
    }
}
