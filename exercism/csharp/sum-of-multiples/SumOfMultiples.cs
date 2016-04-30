using System;
using System.Linq;

namespace Exercism
{
    public static class SumOfMultiples
    {
        public static int To(int [] multiples, int upto)
        {
            return Enumerable.Range(1, upto - 1)
              .Where(divides(multiples))
              .Aggregate(0, (a, b) => a + b);
        }

        private static Func<int, bool> divides(int [] multiples)
        {
            return n => multiples.Where(m => n % m == 0).Count() > 0;
        }
    }
}
