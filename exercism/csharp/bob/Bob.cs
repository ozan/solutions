using System.Text.RegularExpressions;


namespace Exercism
{
    public static class Bob
    {
        public static string Hey(string prompt)
        {
            if (Yelling(prompt)) return "Whoa, chill out!";
            if (Question(prompt)) return "Sure.";
            if (Silence(prompt)) return "Fine. Be that way!";
            return "Whatever.";
        }

        private static bool Yelling(string prompt)
        {
            var alpha = new Regex("[a-zA-Z]");
            return alpha.IsMatch(prompt) && prompt == prompt.ToUpper();
        }

        private static bool Question(string prompt)
        {
            var s = prompt.Trim();
            return s.Length > 0 && s[s.Length - 1] == '?';
        }

        private static bool Silence(string prompt)
        {
            return prompt.Trim() == "";
        }
    }
}
