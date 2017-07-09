import java.util.List;

public class KCombinations {

    private final int[] items;

    KCombinations(int[] items) {
        this.items = items;
    }

    int[][] combinations(int k) { return combinations(k, 0); }

    int[][] combinations(int k, int offset) {
        /*
        Return the n-choose-k many combinations of length k from
        the given items.
        */
        int[][] out = new int[this.nChooseK(items.length - offset, k)][k];

        // Base case: k-many "combinations" of length 1
        if (k == 1) {
            for (int i = offset, j = 0; i < items.length; i++, j++)
                out[j][0] = items[i];
            return out;
        }

        // Recursive case: combine each item with all possible k-1 length
        // combinations chosen from the subarray of items _beyond_ that
        // item. Choose the items _beyond_ the current item in order to
        // avoid duplication.
        for (int i = offset, outI = 0; i < items.length; i++) {
            int[][] subCombinations = combinations(k - 1, i + 1);
            for (int j = 0; j < subCombinations.length; j++) {
                out[outI][0] = items[i];
                for (int jj = 0; jj < k - 1; jj++)
                    out[outI][jj + 1] = subCombinations[j][jj];
                outI++;
            }
        }
        return out;
    }

    int nChooseK (int n, int k) {
        int res = 1;
        for (int i = n, nmk = n - k; i > nmk; i--) res *= i;
        while (k > 1) res /= k--;
        return res;
    }
}
