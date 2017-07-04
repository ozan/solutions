public class DifferenceOfSquaresCalculator {

    int computeSquareOfSumTo(int n) {
        int sum = n * (n + 1) >> 1;
        return sum * sum;
    }

    int computeSumOfSquaresTo(int n) {
        return n * (n + 1) * (2 * n + 1) / 6;
    }

    int computeDifferenceOfSquares(int n) {
        return this.computeSquareOfSumTo(n) - this.computeSumOfSquaresTo(n);
    }
}
