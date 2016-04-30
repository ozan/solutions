using NUnit.Framework;

using Exercism;

[TestFixture]
public class HammingTest
{
    [Test]
    public void No_difference_between_empty_strands()
    {
        Assert.That(Hamming.Compute("",""), Is.EqualTo(0));
    }

    [Test]
    public void No_difference_between_identical_strands()
    {
        Assert.That(Hamming.Compute("GGACTGA","GGACTGA"), Is.EqualTo(0));
    }

    [Test]
    public void Complete_hamming_distance_in_small_strand()
    {
        Assert.That(Hamming.Compute("ACT","GGA"), Is.EqualTo(3));
    }

    [Test]
    public void Hamming_distance_is_off_by_one_strand()
    {
        Assert.That(Hamming.Compute("GGACGGATTCTG","AGGACGGATTCT"), Is.EqualTo(9));
    }

    [Test]
    public void Smalling_hamming_distance_in_middle_somewhere()
    {
        Assert.That(Hamming.Compute("GGACG","GGTCG"), Is.EqualTo(1));
    }

    [Test]
    public void Larger_distance()
    {
        Assert.That(Hamming.Compute("ACCAGGG","ACTATGG"), Is.EqualTo(2));
    }
}
