using System;
using System.Collections.Generic;
using System.Linq;

public class Clock : System.Object
{
    public int TotalMinutes;

    public Clock (int hours, int minutes=0)
    {
        TotalMinutes = ClockMod(hours * 60 + minutes);
    }

    public override string ToString()
    {
        return String.Format("{0:d2}:{1:d2}", TotalMinutes / 60, TotalMinutes % 60);
    }

    public Clock Add(int n)
    {
        return new Clock(0, TotalMinutes + n);
    }

    public Clock Subtract(int n)
    {
        return new Clock(0, TotalMinutes - n);
    }

    public override bool Equals (System.Object obj)
    {
        if (obj == null) return false;

        Clock other = obj as Clock;
        if ((System.Object)other == null) return false;

        return TotalMinutes == other.TotalMinutes;
    }

    static int ClockMod(int n)
    {
        int dayMins = 60 * 24;
        return (n % dayMins + dayMins) % dayMins;
    }
}
