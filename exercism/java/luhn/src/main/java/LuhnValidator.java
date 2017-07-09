class LuhnValidator {

    boolean isValid(String candidate) {
        int length = 0, sum = 0;
        int[] map = {
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
            0, 2, 4, 6, 8, 1, 3, 5, 7, 9
        };
        for (int i = candidate.length() - 1; i >= 0; i--) {
            char c = candidate.charAt(i);
            if (c == ' ') continue;
            if (c < '0' || c > '9') return false;
            sum += map[10 * (length++ % 2) + (c - '0')];
        }
        return length > 1 && sum % 10 == 0;
    }

}
