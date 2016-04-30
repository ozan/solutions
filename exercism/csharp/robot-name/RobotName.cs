using System;
using System.Collections.Generic;


namespace Exercism
{
    public class Robot {
        public string Name { get; private set; }
        HashSet<string> used = new HashSet<string>();
        Random random;

        public Robot()
        {
            random = new Random(Guid.NewGuid().GetHashCode());
            Name = randomName();
        }

        public void Reset()
        {
            Name = randomName();
        }

        private string randomName()
        {
            var alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            var numeric = "1234567890";

            var proposedName = String.Concat(new char [] {
                randChoice(alpha),
                randChoice(alpha),
                randChoice(numeric),
                randChoice(numeric),
                randChoice(numeric)
            });

            if (used.Contains(proposedName)) {
                proposedName = randomName();
            }
            used.Add(proposedName);
            return proposedName;
        }

        private char randChoice(string source) {
            return source[random.Next(source.Length)];
        }
    }

}
