using System;
using System.Collections.Generic;

namespace Exercism
{
    public enum TriangleKind
    {
        Equilateral,
        Isosceles,
        Scalene
    };

    public class TriangleException : Exception
    {
    }

    public static class Triangle
    {
        static Dictionary<int, TriangleKind> kindForSideNum = new Dictionary<int, TriangleKind> {
            { 1, TriangleKind.Equilateral },
            { 2, TriangleKind.Isosceles },
            { 3, TriangleKind.Scalene }
        };

        public static TriangleKind Kind(Decimal a, Decimal b, Decimal c)
        {
            // invalid side length
            if (a <= 0 || b <= 0 || c <= 0) throw new TriangleException();

            // breaks triangle inequality
            if (a >= b + c || b >= a + c || c >= a + b) throw new TriangleException();

            var sides = new Decimal [] { a, b, c };
            var sideSet = new HashSet<Decimal>(sides);
            return kindForSideNum[sideSet.Count];
        }
    }
}
