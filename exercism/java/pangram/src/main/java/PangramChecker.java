public class PangramChecker {

    public boolean isPangram(String input) {
        /* Using a bitfield, turn on a bit for each character encountered */
        int bset = 0;
        for (int i = 0, ch; i < input.length(); i++) {
            ch = input.charAt(i);
            if (ch >= 97) ch -= 32;  // make uppercase
            if (ch < 65 || ch > 90) continue;  // skip non-alpha characters
            bset |= 1 << ch - 65;  // turn nth bit on
        }
        return bset == 0x03ffffff;  // is pangram if lower 26 bits are on
    }

}
