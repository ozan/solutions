// Version: 1.2.0

#include "vendor/unity.h"

#define BUFFER_SIZE 256

extern void two_fer(const char *name, char *buffer);

void setUp(void) {
}

void tearDown(void) {
}

void test_no_name_given(void) {
    char buffer[BUFFER_SIZE];

    two_fer(NULL, buffer);
    TEST_ASSERT_EQUAL_STRING("One for you, one for me.", buffer);
}

void test_a_name_given(void) {
    char buffer[BUFFER_SIZE];

    two_fer("Alice", buffer);
    TEST_ASSERT_EQUAL_STRING("One for Alice, one for me.", buffer);
}

void test_another_name_given(void) {
    char buffer[BUFFER_SIZE];

    two_fer("Bob", buffer);
    TEST_ASSERT_EQUAL_STRING("One for Bob, one for me.", buffer);
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_no_name_given);
    RUN_TEST(test_a_name_given);
    RUN_TEST(test_another_name_given);
    return UNITY_END();
}
