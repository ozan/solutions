using System;
using System.Collections.Generic;
using System.Linq;


public class Raindrops
{
    public static string Convert (int n)
    {
        var plxngs = new List<Plxng> {
            new Plxng("Pling", 3),
            new Plxng("Plang", 5),
            new Plxng("Plong", 7)
        }
        .Where(p => n % p.val == 0)
        .Select(p => p.name);

        return plxngs.Count() == 0 ? n.ToString() : String.Join("", plxngs);

    }

    class Plxng
    {
        public string name;
        public int val;

        public Plxng (string name, int val) {
            this.name = name;
            this.val = val;
        }
    }
}
