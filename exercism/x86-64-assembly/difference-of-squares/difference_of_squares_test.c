// Version: 1.2.0

#include "vendor/unity.h"

extern int square_of_sum(int number);
extern int sum_of_squares(int number);
extern int difference_of_squares(int number);

void setUp(void) {
}

void tearDown(void) {
}

void test_square_of_sum_1(void) {
    TEST_ASSERT_EQUAL_INT(1, square_of_sum(1));
}

void test_square_of_sum_5(void) {
    TEST_ASSERT_EQUAL_INT(225, square_of_sum(5));
}

void test_square_of_sum_100(void) {
    TEST_ASSERT_EQUAL_INT(25502500, square_of_sum(100));
}

void test_sum_of_squares_1(void) {
    TEST_ASSERT_EQUAL_INT(1, sum_of_squares(1));
}

void test_sum_of_squares_5(void) {
    TEST_ASSERT_EQUAL_INT(55, sum_of_squares(5));
}

void test_sum_of_squares_100(void) {
    TEST_ASSERT_EQUAL_INT(338350, sum_of_squares(100));
}

void test_difference_of_squares_1(void) {
    TEST_ASSERT_EQUAL_INT(0, difference_of_squares(1));
}

void test_difference_of_squares_5(void) {
    TEST_ASSERT_EQUAL_INT(170, difference_of_squares(5));
}

void test_difference_of_squares_100(void) {
    TEST_ASSERT_EQUAL_INT(25164150, difference_of_squares(100));
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_square_of_sum_1);
    RUN_TEST(test_square_of_sum_5);
    RUN_TEST(test_square_of_sum_100);
    RUN_TEST(test_sum_of_squares_1);
    RUN_TEST(test_sum_of_squares_5);
    RUN_TEST(test_sum_of_squares_100);
    RUN_TEST(test_difference_of_squares_1);
    RUN_TEST(test_difference_of_squares_5);
    RUN_TEST(test_difference_of_squares_100);
    return UNITY_END();
}
