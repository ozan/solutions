using System.Linq;
using System.Text.RegularExpressions;

namespace Exercism
{
    public static class Binary
    {
        public static int ToDecimal(string binary)
        {
            Regex valid = new Regex(@"^[10]*$");
            if (!valid.IsMatch(binary)) return 0;

            return binary.Reverse()
              .Select(ch => ch == '1' ? 1 : 0)
              .Select((ch, i) => ch == 1 ? 1 << i : 0)
              .Aggregate(0, (a, b) => a + b);
        }
    }
}
