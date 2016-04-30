using System.Collections.Generic;
using System.Linq;


namespace Exercism
{
    public class School
    {
        public Dictionary<int, List<string>> Roster = new Dictionary<int, List<string>>();

        public void Add(string name, int grade)
        {
            if (!Roster.ContainsKey(grade)) Roster[grade] = new List<string>();
            Roster[grade].Add(name);
            Roster[grade] = Roster[grade].OrderBy(n => n).ToList();
        }

        public List<string> Grade(int grade)
        {
            if (!Roster.ContainsKey(grade)) return new List<string>();
            return Roster[grade];
        }
    }
}
