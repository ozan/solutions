namespace Exercism
{
    using NUnit.Framework;

    [TestFixture]
    public class AcronymTest
    {
        [Test]
        public void Empty_string_abbreviated_to_empty_string()
        {
            Assert.That(Acronym.Abbreviate(string.Empty), Is.EqualTo(string.Empty));
        }

        [TestCase("Portable Network Graphics", ExpectedResult = "PNG")]
        [TestCase("Ruby on Rails", ExpectedResult = "ROR")]
        [TestCase("HyperText Markup Language", ExpectedResult = "HTML")]
        [TestCase("First In, First Out", ExpectedResult = "FIFO")]
        [TestCase("PHP: Hypertext Preprocessor", ExpectedResult = "PHP")]
        [TestCase("Complementary metal-oxide semiconductor", ExpectedResult = "CMOS")]
        public string Phrase_abbreviated_to_acronym(string phrase)
        {
            return Acronym.Abbreviate(phrase);
        }
    }
}
