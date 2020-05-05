// Version: 1.2.0

#include "vendor/unity.h"

enum planet {
    MERCURY,
    VENUS,
    EARTH,
    MARS,
    JUPITER,
    SATURN,
    URANUS,
    NEPTUNE
};

extern float age(enum planet planet, int seconds);

void setUp(void) {
}

void tearDown(void) {
}

void test_age_on_earth(void) {
    TEST_ASSERT_FLOAT_WITHIN(0.01, 31.69, age(EARTH, 1000000000));
}

void test_age_on_mercury(void) {
    TEST_ASSERT_FLOAT_WITHIN(0.01, 280.88, age(MERCURY, 2134835688));
}

void test_age_on_venus(void) {
    TEST_ASSERT_FLOAT_WITHIN(0.01, 9.78, age(VENUS, 189839836));
}

void test_age_on_mars(void) {
    TEST_ASSERT_FLOAT_WITHIN(0.01, 35.88, age(MARS, 2129871239));
}

void test_age_on_jupiter(void) {
    TEST_ASSERT_FLOAT_WITHIN(0.01, 2.41, age(JUPITER, 901876382));
}

void test_age_on_saturn(void) {
    TEST_ASSERT_FLOAT_WITHIN(0.01, 2.15, age(SATURN, 2000000000));
}

void test_age_on_uranus(void) {
    TEST_ASSERT_FLOAT_WITHIN(0.01, 0.46, age(URANUS, 1210123456));
}

void test_age_on_neptune(void) {
    TEST_ASSERT_FLOAT_WITHIN(0.01, 0.35, age(NEPTUNE, 1821023456));
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_age_on_earth);
    RUN_TEST(test_age_on_mercury);
    RUN_TEST(test_age_on_venus);
    RUN_TEST(test_age_on_mars);
    RUN_TEST(test_age_on_jupiter);
    RUN_TEST(test_age_on_saturn);
    RUN_TEST(test_age_on_uranus);
    RUN_TEST(test_age_on_neptune);
    return UNITY_END();
}
