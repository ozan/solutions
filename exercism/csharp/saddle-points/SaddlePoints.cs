using System;
using System.Collections.Generic;
using System.Linq;

public class SaddlePoints
{
    int[,] Values;
    int[] RowMaxes;
    int[] ColMins;

    public SaddlePoints (int[,] values)
    {
        var rowCount = values.GetLength(0);
        var colCount = values.GetLength(1);
        var flatVals = values.Cast<int>();

        Values = values;
        RowMaxes = Enumerable.Range(0, rowCount).Select(
          idx => flatVals.Skip(idx * colCount).Take(colCount).Max()
        ).ToArray();
        ColMins = Enumerable.Range(0, colCount).Select(
          (idx) => flatVals.Where((_, i) => i % colCount == idx).Min()
        ).ToArray();
    }

    public IEnumerable<Tuple<int, int>> Calculate ()
    {
        foreach (var t in Coords(RowMaxes.Length, ColMins.Length)) {
            var val = Values[t.Item1, t.Item2];
            if (val == RowMaxes[t.Item1] && val == ColMins[t.Item2]) {
              yield return t;
            }
        }
    }

    static IEnumerable<Tuple<int, int>> Coords (int m, int n)
    {
      for (int i = 0; i < m; i++) {
          for (int j = 0; j < n; j++) {
              yield return Tuple.Create(i, j);
          }
      }
    }

}
