using NUnit.Framework;

[TestFixture]
public class OctalTest
{
    [TestCase("1", ExpectedResult = 1)]
    [TestCase("10", ExpectedResult = 8)]
    [TestCase("17", ExpectedResult = 15)]
    [TestCase("11", ExpectedResult = 9)]
    [TestCase("130", ExpectedResult = 88)]
    [TestCase("2047", ExpectedResult = 1063)]
    [TestCase("7777", ExpectedResult = 4095)]
    [TestCase("1234567", ExpectedResult = 342391)]
    public int Octal_converts_to_decimal(string value)
    {
        return Octal.ToDecimal(value);
    }

    [TestCase("carrot")]
    [TestCase("8")]
    [TestCase("9")]
    [TestCase("6789")]
    [TestCase("abc1z")]
    public void Invalid_octal_is_decimal_0(string invalidValue)
    {
        Assert.That(Octal.ToDecimal(invalidValue), Is.EqualTo(0));
    }

    [Test]
    public void Octal_can_convert_formatted_strings()
    {
        Assert.That(Octal.ToDecimal("011"), Is.EqualTo(9));
    }
}
