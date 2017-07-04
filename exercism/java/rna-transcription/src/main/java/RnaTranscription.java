public class RnaTranscription {
    public String transcribe(String dnaStrand) {
        String key = "U.G...C............A";
        int n = dnaStrand.length();
        
        char[] out = new char[n];
        for (int i = 0; i < n; i++)
            out[i] = key.charAt((int) dnaStrand.charAt(i) - 65);

        return new String(out);
    }
}
