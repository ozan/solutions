using System;
using System.Collections.Generic;
using System.Linq;

public class Squares
{
    int N;

    public Squares(int n)
    {
        if (n < 0) throw new ArgumentException();
        N = n;
    }

    public int SumOfSquares()
    {
        return Enumerable.Range(1, N).Select(Square).Sum();
    }

    public int SquareOfSums()
    {
        return Square(Enumerable.Range(1, N).Sum());
    }

    public int DifferenceOfSquares()
    {
        return SquareOfSums() - SumOfSquares();
    }

    private static int Square(int n)
    {
        return n * n;
    }
}
