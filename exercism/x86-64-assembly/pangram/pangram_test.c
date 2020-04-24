// Version: 2.0.0

#include "vendor/unity.h"

extern int is_pangram(const char *str);

void setUp(void) {
}

void tearDown(void) {
}

void test_empty_sentence(void) {
    TEST_ASSERT_FALSE(is_pangram(""));
}

void test_perfect_lower_case(void) {
    TEST_ASSERT_TRUE(is_pangram("abcdefghijklmnopqrstuvwxyz"));
}

void test_only_lower_case(void) {
    TEST_ASSERT_TRUE(is_pangram("the quick brown fox jumps over the lazy dog"));
}

void test_missing_the_letter_x(void) {
    TEST_ASSERT_FALSE(is_pangram("a quick movement of the enemy will jeopardize five gunboats"));
}

void test_missing_the_letter_h(void) {
    TEST_ASSERT_FALSE(is_pangram("five boxing wizards jump quickly at it"));
}

void test_with_underscores(void) {
    TEST_ASSERT_TRUE(is_pangram("the_quick_brown_fox_jumps_over_the_lazy_dog"));
}

void test_with_numbers(void) {
    TEST_ASSERT_TRUE(is_pangram("the 1 quick brown fox jumps over the 2 lazy dogs"));
}

void test_missing_letters_replaced_by_numbers(void) {
    TEST_ASSERT_FALSE(is_pangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog"));
}

void test_mixed_case_and_punctuation(void) {
    TEST_ASSERT_TRUE(is_pangram("\"Five quacking Zephyrs jolt my wax bed.\""));
}

void test_case_insensitive(void) {
    TEST_ASSERT_FALSE(is_pangram("the quick brown fox jumps over with lazy FX"));
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_empty_sentence);
    RUN_TEST(test_perfect_lower_case);
    RUN_TEST(test_only_lower_case);
    RUN_TEST(test_missing_the_letter_x);
    RUN_TEST(test_missing_the_letter_h);
    RUN_TEST(test_with_underscores);
    RUN_TEST(test_with_numbers);
    RUN_TEST(test_missing_letters_replaced_by_numbers);
    RUN_TEST(test_mixed_case_and_punctuation);
    RUN_TEST(test_case_insensitive);
    return UNITY_END();
}
