// Version: 1.7.0

#include "vendor/unity.h"

extern int is_isogram(const char *str);

void setUp(void) {
}

void tearDown(void) {
}

void test_empty_string(void) {
    TEST_ASSERT_TRUE(is_isogram(""));
}

void test_isogram_with_only_lower_case_characters(void) {
    TEST_ASSERT_TRUE(is_isogram("isogram"));
}

void test_word_with_one_duplicated_character(void) {
    TEST_ASSERT_FALSE(is_isogram("eleven"));
}

void test_word_with_one_duplicated_character_from_the_end_of_the_alphabet(void) {
    TEST_ASSERT_FALSE(is_isogram("zzyzx"));
}

void test_longest_reported_english_isogram(void) {
    TEST_ASSERT_TRUE(is_isogram("subdermatoglyphic"));
}

void test_word_with_duplicated_character_in_mixed_case(void) {
    TEST_ASSERT_FALSE(is_isogram("Alphabet"));
}

void test_word_with_duplicated_character_in_mixed_case_lowercase_first(void) {
    TEST_ASSERT_FALSE(is_isogram("alphAbet"));
}

void test_hypothetical_isogrammic_word_with_hyphen(void) {
    TEST_ASSERT_TRUE(is_isogram("thumbscrew-japingly"));
}

void test_hypothetical_word_with_duplicated_character_following_hyphen(void) {
    TEST_ASSERT_FALSE(is_isogram("thumbscrew-jappingly"));
}

void test_isogram_with_duplicated_hyphen(void) {
    TEST_ASSERT_TRUE(is_isogram("six-year-old"));
}

void test_madeup_name_that_is_an_isogram(void) {
    TEST_ASSERT_TRUE(is_isogram("Emily Jung Schwartzkopf"));
}

void test_duplicated_character_in_the_middle(void) {
    TEST_ASSERT_FALSE(is_isogram("accentor"));
}

void test_same_first_and_last_characters(void) {
    TEST_ASSERT_FALSE(is_isogram("angola"));
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_empty_string);
    RUN_TEST(test_isogram_with_only_lower_case_characters);
    RUN_TEST(test_word_with_one_duplicated_character);
    RUN_TEST(test_word_with_one_duplicated_character_from_the_end_of_the_alphabet);
    RUN_TEST(test_longest_reported_english_isogram);
    RUN_TEST(test_word_with_duplicated_character_in_mixed_case);
    RUN_TEST(test_word_with_duplicated_character_in_mixed_case_lowercase_first);
    RUN_TEST(test_hypothetical_isogrammic_word_with_hyphen);
    RUN_TEST(test_hypothetical_word_with_duplicated_character_following_hyphen);
    RUN_TEST(test_isogram_with_duplicated_hyphen);
    RUN_TEST(test_madeup_name_that_is_an_isogram);
    RUN_TEST(test_duplicated_character_in_the_middle);
    RUN_TEST(test_same_first_and_last_characters);
    return UNITY_END();
}
