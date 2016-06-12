using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;

enum Result { Win, Draw, Loss }

class TeamTally
{
    public string Team;
    public int Played;
    public int Win;
    public int Draw;
    public int Loss;
    public int Points;

    public TeamTally (string name)
    {
        Team = name;
    }
}

public class Tournament
{
    static Dictionary<string, Result> Results = new Dictionary<string, Result> {
        { "win", Result.Win },
        { "loss", Result.Loss },
        { "draw", Result. Draw }
    };

    public static void Tally (MemoryStream inStream, MemoryStream outStream)
    {
        var parsed = Parse(new StreamReader(inStream).ReadToEnd());
        var tallied = DoTally(parsed);
        var formatted = Format(tallied);
        var bytes = System.Text.Encoding.UTF8.GetBytes(formatted);
        outStream.Write(bytes, 0, bytes.Length);
    }

    static IEnumerable<Tuple<string, string, Result>> Parse (string input)
    {
        var regex = new Regex(@"(.+);(.+);(win|loss|draw)(\n|$)");
        var matches = regex.Matches(input);
        foreach (Match match in matches)
        {
            var g = match.Groups;
            yield return Tuple.Create(
                g[1].ToString(),
                g[2].ToString(),
                Results[g[3].ToString()]
            );
        }
    }

    static Dictionary<string, TeamTally> DoTally (IEnumerable<Tuple<string, string, Result>> results)
    {
        var d = new Dictionary<string, TeamTally>();
        foreach (var t in results)
        {
            var team = t.Item1;
            var otherTeam = t.Item2;
            var result = t.Item3;
            TeamTally tally, otherTally;
            try {
                tally = d[team];
            } catch (KeyNotFoundException) {
                tally = new TeamTally(team);
                d[team] = tally;
            }
            try {
                otherTally = d[otherTeam];
            } catch (KeyNotFoundException) {
                otherTally = new TeamTally(otherTeam);
                d[otherTeam] = otherTally;
            }

            tally.Played += 1;
            otherTally.Played += 1;
            if (result == Result.Win) {
                tally.Win += 1;
                tally.Points += 3;
                otherTally.Loss += 1;
            } else if (result == Result.Loss) {
                tally.Loss += 1;
                otherTally.Win += 1;
                otherTally.Points += 3;
            } else {
                tally.Draw += 1;
                tally.Points += 1;
                otherTally.Draw += 1;
                otherTally.Points += 1;
            }
        }
        return d;
    }

    static string Format (Dictionary<string, TeamTally> tallies)
    {
        var title = "Team                           | MP |  W |  D |  L |  P\n";
        var template = "{0,-30} | {1,2} | {2,2} | {3,2} | {4,2} | {5,2}";
        var lines = tallies.Values
            .OrderByDescending(t => t.Points)
            .Select(t => String.Format(template, t.Team, t.Played, t.Win, t.Draw, t.Loss, t.Points));
        return title + String.Join("\n", lines);
    }
}
