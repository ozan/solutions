class Scrabble {

    private final String word;
    private static final int[] VALUES = {
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  1,  3,  3,  2,  1,  4,  2,  4,  1,  8,  5,  1,  3,  1,  1,
        3, 10,  1,  1,  1,  1,  4,  4,  8,  4, 10,  0,  0,  0,  0,  0,
        0,  1,  3,  3,  2,  1,  4,  2,  4,  1,  8,  5,  1,  3,  1,  1,
        3, 10,  1,  1,  1,  1,  4,  4,  8,  4, 10,  0,  0,  0,  0,  0,
    };

    Scrabble(String word) {
        this.word = word;
    }

    int getScore() {
        int score = 0, n = this.word.length();
        for (int i = 0; i < n; i++)
            score += VALUES[this.word.charAt(i)];
        return score;
    }

}
