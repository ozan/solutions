// Version: 2.3.0

#include "vendor/unity.h"

extern int distance(const char *strand1, const char *strand2);

void setUp(void) {
}

void tearDown(void) {
}

void test_empty_strands(void) {
    TEST_ASSERT_EQUAL_INT(0, distance("", ""));
}

void test_single_letter_identical_strands(void) {
    TEST_ASSERT_EQUAL_INT(0, distance("A", "A"));
}

void test_single_letter_different_strands(void) {
    TEST_ASSERT_EQUAL_INT(1, distance("G", "T"));
}

void test_long_identical_strands(void) {
    TEST_ASSERT_EQUAL_INT(0, distance("GGACTGAAATCTG", "GGACTGAAATCTG"));
}

void test_long_different_strands(void) {
    TEST_ASSERT_EQUAL_INT(9, distance("GGACGGATTCTG", "AGGACGGATTCT"));
}

void test_disallow_first_strand_longer(void) {
    TEST_ASSERT_EQUAL_INT(-1, distance("AATG", "AAA"));
}

void test_disallow_second_strand_longer(void) {
    TEST_ASSERT_EQUAL_INT(-1, distance("ATA", "AGTG"));
}

void test_disallow_left_empty_strand(void) {
    TEST_ASSERT_EQUAL_INT(-1, distance("", "G"));
}

void test_disallow_right_empty_strand(void) {
    TEST_ASSERT_EQUAL_INT(-1, distance("G", ""));
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_empty_strands);
    RUN_TEST(test_single_letter_identical_strands);
    RUN_TEST(test_single_letter_different_strands);
    RUN_TEST(test_long_identical_strands);
    RUN_TEST(test_long_different_strands);
    RUN_TEST(test_disallow_first_strand_longer);
    RUN_TEST(test_disallow_second_strand_longer);
    RUN_TEST(test_disallow_left_empty_strand);
    RUN_TEST(test_disallow_right_empty_strand);
    return UNITY_END();
}
