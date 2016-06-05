using System;
using System.Collections.Generic;
using System.Linq;

public class Cipher
{
    public string Key;

    public Cipher ()
    {
        var r = new Random(Guid.NewGuid().GetHashCode());
        var cipherChars = new int[100].Select(_ => (char)('a' + r.Next(0, 26)));
        Key = String.Concat(cipherChars);
    }

    public Cipher (string key)
    {
        if (key.Length == 0 ||
            key.Where(ch => !Char.IsLower(ch) || !Char.IsLetter(ch)).Any()) {
            throw new ArgumentException();
        }
        Key = key;
    }

    public IEnumerable<char> Encode (IEnumerable<char> given)
    {
        return given.Select((ch, i) => (char)('a' + (ch + Key[i % Key.Length] - 'a' - 'a') % 26));
    }

    public IEnumerable<char> Decode (IEnumerable<char> given)
    {
        return given.Zip(Key, (a, b) => (char)((26 + a - b) % 26 + 'a'));
    }
}
