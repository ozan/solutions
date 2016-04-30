using System.Collections.Generic;


namespace Exercism
{
    public static class ETL
    {
        public static Dictionary<string, int> Transform(Dictionary<int, IList<string>> old)
        {
            var transformed = new Dictionary<string, int>();
            foreach (KeyValuePair<int, IList<string>> e in old) {
                foreach (var piece in e.Value) {
                    transformed.Add(piece.ToLower(), e.Key);
                }
            }
            return transformed;
        }
    }
}
