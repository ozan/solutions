using System;

namespace Exercism
{
    public static class Gigasecond
    {
        public static DateTime Date(DateTime start)
        {
            return start.AddSeconds(1e9);
        }
    }
}
