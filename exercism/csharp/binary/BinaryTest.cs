using NUnit.Framework;

using Exercism;

[TestFixture]
public class BinaryTest
{

    [Test]
    public void Binary_converts_to_decimal()
    {
        var cases = new [] {
            new { bin = "1", dec = 1 },
            new { bin = "10", dec = 2 },
            new { bin = "11", dec = 3 },
            new { bin = "100", dec = 4 },
            new { bin = "1001", dec = 9 },
            new { bin = "11010", dec = 26 },
            new { bin = "10001101000", dec = 1128 }
        };
        foreach (var tc in cases) {
            Assert.That(Binary.ToDecimal(tc.bin), Is.EqualTo(tc.dec));
        }
    }

    [Test]
    public void Invalid_binary_is_decimal_0()
    {

        var cases = new string [] {
          "carrot",
          "2",
          "5",
          "9",
          "a10",
          "100b",
          "10c01",
          "134678",
          "abc10z",
        };

        foreach (var invalid in cases) {
            Assert.That(Binary.ToDecimal(invalid), Is.EqualTo(0));
        }
    }

    [Test]
    public void Binary_can_convert_formatted_strings()
    {
        Assert.That(Binary.ToDecimal("011"), Is.EqualTo(3));
    }
}
