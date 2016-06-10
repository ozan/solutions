using System;
using System.Collections.Generic;
using System.Linq;

public class Matrix
{
    public int Rows;
    public int Cols;

    int[][] Values;
    int[][] Transpose;

    public Matrix (string input)
    {
        Values = input
            .Split('\n')
            .Select(row => row.Split(' ').Select(Int32.Parse).ToArray())
            .ToArray();
        Transpose = Values[0]
            .Select((_, i) => Values.Select(row => row[i]).ToArray())
            .ToArray();
        Rows = Values.Length;
        Cols = Transpose.Length;
    }

    public int[] Row (int idx)
    {
        return Values[idx];
    }

    public int[] Col (int idx)
    {
        return Transpose[idx];
    }
}
