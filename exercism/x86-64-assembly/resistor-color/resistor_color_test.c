// Version: 1.0.0

#include "vendor/unity.h"

#define ARRAY_SIZE(x) (sizeof(x) / sizeof((x)[0]))

extern int color_code(const char *color);
extern const char **colors(void);

void setUp(void) {
}

void tearDown(void) {
}

void test_black(void) {
    TEST_ASSERT_EQUAL_INT(0, color_code("black"));
}

void test_white(void) {
    TEST_ASSERT_EQUAL_INT(9, color_code("white"));
}

void test_orange(void) {
    TEST_ASSERT_EQUAL_INT(3, color_code("orange"));
}

void test_invalid(void) {
    TEST_ASSERT_EQUAL_INT(-1, color_code("foo"));
}

void test_colors(void) {
    const char **color_array = colors();
    const char *expected[] = {"black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"};
    int size;

    for (size = 0; color_array[size]; size++) {
    }
    TEST_ASSERT_EQUAL_INT(ARRAY_SIZE(expected), size);
    TEST_ASSERT_EQUAL_STRING_ARRAY(expected, color_array, size);
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_black);
    RUN_TEST(test_white);
    RUN_TEST(test_orange);
    RUN_TEST(test_colors);
    RUN_TEST(test_invalid);
    return UNITY_END();
}
