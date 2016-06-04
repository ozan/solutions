using System;
using System.Collections.Generic;
using System.Linq;

public class Allergies
{
    private List<string> allergens;
    private int score;

    public Allergies(int score)
    {
        this.allergens = new List<string> {
          "eggs",
          "peanuts",
          "shellfish",
          "strawberries",
          "tomatoes",
          "chocolate",
          "pollen",
          "cats"
        };
        this.score = score;
    }

    public bool AllergicTo (string allergen)
    {
        return (1 << allergens.IndexOf(allergen) & score) > 0;
    }

    public IEnumerable<string> List ()
    {
        return allergens.Where((_, i) => (1 << i & score) > 0);
    }
}
