import org.junit.Ignore;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.ExpectedException;

import static org.junit.Assert.assertEquals;

/*
 * version: 1.1.0
 */
public class HammingTest {

    @Rule
    public ExpectedException expectedException = ExpectedException.none();

    @Test
    public void testNoDistanceBetweenEmptyStrands() {
        assertEquals(0, new Hamming("", "").getHammingDistance());
    }

    @Test
    public void testNoDistanceBetweenShortIdenticalStrands() {
        assertEquals(0, new Hamming("A", "A").getHammingDistance());
    }

    @Test
    public void testNoDistanceBetweenLongIdenticalStrands() {
        assertEquals(0, new Hamming("GGACTGA", "GGACTGA").getHammingDistance());
    }

    @Test
    public void testCompleteDistanceInSingleNucleotideStrand() {
        assertEquals(1, new Hamming("A", "G").getHammingDistance());
    }

    @Test
    public void testCompleteDistanceInSmallStrand() {
        assertEquals(2, new Hamming("AG", "CT").getHammingDistance());
    }

    @Test
    public void testSmallDistanceInSmallStrand() {
        assertEquals(1, new Hamming("AT", "CT").getHammingDistance());
    }

    @Test
    public void testSmallDistanceInMediumStrand() {
        assertEquals(1, new Hamming("GGACG", "GGTCG").getHammingDistance());
    }

    @Test
    public void testSmallDistanceInLongStrand() {
        assertEquals(2, new Hamming("ACCAGGG", "ACTATGG").getHammingDistance());
    }

    @Test
    public void testNonUniqueCharacterInFirstStrand() {
        assertEquals(1, new Hamming("AGA", "AGG").getHammingDistance());
    }

    @Test
    public void testNonUniqueCharacterInSecondStrand() {
        assertEquals(1, new Hamming("AGG", "AGA").getHammingDistance());
    }

    @Test
    public void testSameNucleotidesInDifferentPositions() {
        assertEquals(2, new Hamming("TAG", "GAT").getHammingDistance());
    }

    @Test
    public void testLargeDistanceInPermutedStrand() {
        assertEquals(4, new Hamming("GATACA", "GCATAA").getHammingDistance());
    }

    @Test
    public void testLargeDistanceInOffByOneStrand() {
        assertEquals(9, new Hamming("GGACGGATTCTG", "AGGACGGATTCT").getHammingDistance());
    }

    @Test
    public void testValidatesFirstStrandNotLonger() {
        expectedException.expect(IllegalArgumentException.class);
        expectedException.expectMessage("leftStrand and rightStrand must be of equal length.");

        new Hamming("AATG", "AAA");
    }

    @Test
    public void testValidatesSecondStrandNotLonger() {
        expectedException.expect(IllegalArgumentException.class);
        expectedException.expectMessage("leftStrand and rightStrand must be of equal length.");

        new Hamming("ATA", "AGTG");
    }

}
