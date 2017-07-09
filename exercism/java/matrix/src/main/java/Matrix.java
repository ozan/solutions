public class Matrix {

    private int[] matrix;
    private int numRows = 0;
    private int numColumns;

    Matrix(String str) {
        int numElements = 0, len = str.length();
        matrix = new int[len];  // can't have more elements than chars
        int val = 0;
        for (int i = 0; i < len; i++) {
            char c = str.charAt(i);
            if (c == '\n' || c == ' ') {
                matrix[numElements++] = val;
                val = 0;
                if (c == '\n') numRows++;
            } else {
                val = 10 * val + (c - '0');
            }
        }
        matrix[numElements++] = val;
        numRows++;
        numColumns = numElements / numRows;
    }

    int getColumnsCount() {
        return numColumns;
    }

    int getRowsCount() {
        return numRows;
    }

    int[] getRow(int n) {
        int[] row = new int[numColumns];
        for (int i = 0; i < numColumns; i++)
            row[i] = matrix[n * numColumns + i];
        return row;
    }

    int[] getColumn(int n) {
        int[] column = new int[numRows];
        for (int i = 0; i < numRows; i++)
            column[i] = matrix[numColumns * i + n];
        return column;
    }
}
