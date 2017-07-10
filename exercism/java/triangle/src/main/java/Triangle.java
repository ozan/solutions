class Triangle {

    private final double a, b, c;

    Triangle(double side1, double side2, double side3) throws TriangleException {
        a = side1;
        b = side2;
        c = side3;
        if (a <= 0 || b <= 0 || c <= 0 || a + b <= c || a + c <= b || b + c <= a)
            throw new TriangleException();
    }

    TriangleKind getKind() {
        if (a == b && b == c) return TriangleKind.EQUILATERAL;
        if (a == b || b == c || a == c) return TriangleKind.ISOSCELES;
        return TriangleKind.SCALENE;
    }

}
