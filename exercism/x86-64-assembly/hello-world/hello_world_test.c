// Version: 1.1.0

#include "vendor/unity.h"

extern const char *hello(void);

void setUp(void) {
}

void tearDown(void) {
}

void test_say_hi(void) {
    TEST_ASSERT_EQUAL_STRING("Hello, World!", hello());
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_say_hi);
    return UNITY_END();
}
