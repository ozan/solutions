using System;
using System.Collections.Generic;
using System.Linq;

public class SecretHandshake
{
    static string[] Actions = {
      "wink",
      "double blink",
      "close your eyes",
      "jump"
    };

    public static IEnumerable<string> Commands(int n)
    {
        var actions = Actions.Where((x, i) => (1 << i & n) > 0);
        return (1 << 4 & n) > 0 ? actions.Reverse() : actions;
    }
}
