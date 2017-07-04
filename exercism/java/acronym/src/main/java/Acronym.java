class Acronym {

    private final String phrase;

    Acronym(String phrase) {
        this.phrase = phrase;
    }

    String get() {
        int n = this.phrase.length();
        char[] out = new char[n];  // output
        int op = 0;  // output pointer
        char ch, prior = ' ';
        for (int ip = 0; ip < n; ip++) {
            ch = this.phrase.charAt(ip);
            if (prior == ' ' || prior == '-')
                out[op++] = Character.toUpperCase(ch);
            prior = ch;
        }
        return new String(out, 0, op);
    }

}
