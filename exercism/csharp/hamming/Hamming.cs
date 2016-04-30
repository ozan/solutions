using System.Linq;

namespace Exercism
{
    public static class Hamming
    {
        public static int Compute(string xs, string ys)
        {
            return (from result in xs.Zip(ys, (x, y) => x == y)
                    where result == false
                    select result).Count();
        }
    }
}
