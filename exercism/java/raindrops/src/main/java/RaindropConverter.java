class RaindropConverter {

    String convert(int number) {
        char[] template = { 'P', 'l', '_', 'n', 'g', 'P', 'l', '_', 'n', 'g', 'P', 'l', '_', 'n', 'g' };
        int n = 0;
        if (number % 3 == 0) template[n++ * 5 + 2] = 'i';
        if (number % 5 == 0) template[n++ * 5 + 2] = 'a';
        if (number % 7 == 0) template[n++ * 5 + 2] = 'o';
        if (n == 0) return Integer.toString(number);
        return new String(template, 0, n * 5);
    }

}
