// Version: 1.2.0

#include "vendor/unity.h"

extern void reverse(char *str);

void setUp(void) {
}

void tearDown(void) {
}

void test_an_empty_string(void) {
    char str[] = "";

    reverse(str);
    TEST_ASSERT_EQUAL_STRING("", str);
}

void test_a_word(void) {
    char str[] = "robot";

    reverse(str);
    TEST_ASSERT_EQUAL_STRING("tobor", str);
}

void test_a_capitalized_word(void) {
    char str[] = "Ramen";

    reverse(str);
    TEST_ASSERT_EQUAL_STRING("nemaR", str);
}

void test_a_sentence_with_punctuation(void) {
    char str[] = "I'm hungry!";

    reverse(str);
    TEST_ASSERT_EQUAL_STRING("!yrgnuh m'I", str);
}

void test_a_palindrome(void) {
    char str[] = "racecar";

    reverse(str);
    TEST_ASSERT_EQUAL_STRING("racecar", str);
}

void test_an_evensized_word(void) {
    char str[] = "drawer";

    reverse(str);
    TEST_ASSERT_EQUAL_STRING("reward", str);
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_an_empty_string);
    RUN_TEST(test_a_word);
    RUN_TEST(test_a_capitalized_word);
    RUN_TEST(test_a_sentence_with_punctuation);
    RUN_TEST(test_a_palindrome);
    RUN_TEST(test_an_evensized_word);
    return UNITY_END();
}
