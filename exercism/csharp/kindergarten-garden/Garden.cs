using System;
using System.Collections.Generic;
using System.Linq;

public enum Plant { Clover, Grass, Radishes, Violets };

public class Garden
{
    string[] Names;
    static string[] DefaultNames = new string[] {
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Fred",
        "Ginny",
        "Harriet",
        "Ileana",
        "Joseph",
        "Kincaid",
        "Larry"
    };
    Dictionary<char, Plant> Plants = new Dictionary<char, Plant> {
        { 'C', Plant.Clover },
        { 'G', Plant.Grass },
        { 'R', Plant.Radishes },
        { 'V', Plant.Violets }
    };
    Dictionary<string, Plant[]> PlantsForName;

    public Garden (string[] names, string configuration)
    {
        Names = names;
        Array.Sort(Names);
        PlantsForName = new Dictionary<string, Plant[]>();
        var rows = configuration.Split('\n');
        var row1 = rows[0];
        var row2 = rows[1];
        for (var i = 0; i < row1.Length; i+=2)
        {
            PlantsForName[names[i / 2]] = new Plant[] {
                Plants[row1[i]],
                Plants[row1[i + 1]],
                Plants[row2[i]],
                Plants[row2[i + 1]]
            };
        }
    }

    public static Garden DefaultGarden (string configuration)
    {
        return new Garden(DefaultNames, configuration);
    }

    public Plant[] GetPlants (string name)
    {
        Plant[] value;
        return PlantsForName.TryGetValue(name, out value) ? value : new Plant[0];
    }
}
