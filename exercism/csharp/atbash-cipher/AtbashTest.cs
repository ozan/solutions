using NUnit.Framework;

[TestFixture]
public class AtbashTest
{
    // change Ignore to false to run test case or just remov'
    [TestCase("no", ExpectedResult = "ml")]
    [TestCase("yes", ExpectedResult = "bvh")]
    [TestCase("OMG", ExpectedResult = "lnt")]
    [TestCase("mindblowingly", ExpectedResult = "nrmwy oldrm tob")]
    [TestCase("Testing, 1 2 3, testing.", ExpectedResult = "gvhgr mt123 gvhgr mt")]
    [TestCase("Truth is fiction.", ExpectedResult = "gifgs rhurx grlm")]
    [TestCase("The quick brown fox jumps over the lazy dog.", ExpectedResult = "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt")]
    public string Encodes_words_using_atbash_cipher(string words)
    {
        return Atbash.Encode(words);
    }
}
