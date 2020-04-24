// Version: 1.3.0

#include "vendor/unity.h"

#define BUFFER_SIZE 256

extern void to_rna(const char *strand, char *buffer);

void setUp(void) {
}

void tearDown(void) {
}

void test_empty_rna_sequence(void) {
    char buffer[BUFFER_SIZE];

    to_rna("", buffer);
    TEST_ASSERT_EQUAL_STRING("", buffer);
}

void test_rna_complement_of_cytosine_is_guanine(void) {
    char buffer[BUFFER_SIZE];

    to_rna("C", buffer);
    TEST_ASSERT_EQUAL_STRING("G", buffer);
}

void test_rna_complement_of_guanine_is_cytosine(void) {
    char buffer[BUFFER_SIZE];

    to_rna("G", buffer);
    TEST_ASSERT_EQUAL_STRING("C", buffer);
}

void test_rna_complement_of_thymine_is_adenine(void) {
    char buffer[BUFFER_SIZE];

    to_rna("T", buffer);
    TEST_ASSERT_EQUAL_STRING("A", buffer);
}

void test_rna_complement_of_adenine_is_uracil(void) {
    char buffer[BUFFER_SIZE];

    to_rna("A", buffer);
    TEST_ASSERT_EQUAL_STRING("U", buffer);
}

void test_rna_complement(void) {
    char buffer[BUFFER_SIZE];

    to_rna("ACGTGGTCTTAA", buffer);
    TEST_ASSERT_EQUAL_STRING("UGCACCAGAAUU", buffer);
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_empty_rna_sequence);
    RUN_TEST(test_rna_complement_of_cytosine_is_guanine);
    RUN_TEST(test_rna_complement_of_guanine_is_cytosine);
    RUN_TEST(test_rna_complement_of_thymine_is_adenine);
    RUN_TEST(test_rna_complement_of_adenine_is_uracil);
    RUN_TEST(test_rna_complement);
    return UNITY_END();
}
