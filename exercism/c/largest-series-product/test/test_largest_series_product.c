#include "../src/largest_series_product.h"
#include "vendor/unity.h"

void setUp(void) {}

void tearDown(void) {}

void test_can_find_the_largest_product_of_2_with_numbers_in_order(void) {
  TEST_ASSERT_EQUAL(72, largest_series_product("0123456789", 2));
}

void test_can_find_the_largest_product_of_2(void) {
  TEST_ASSERT_EQUAL(48, largest_series_product("576802143", 2));
}

void test_finds_the_largest_product_if_span_equals_length(void) {
  TEST_ASSERT_EQUAL(18, largest_series_product("29", 2));
}

void test_can_find_the_largest_product_of_3_with_numbers_in_order(void) {
  TEST_ASSERT_EQUAL(504, largest_series_product("0123456789", 3));
}

void test_can_find_the_largest_product_of_3(void) {
  TEST_ASSERT_EQUAL(270, largest_series_product("1027839564", 3));
}

void test_can_find_the_largest_product_of_5_with_numbers_in_order(void) {
  TEST_ASSERT_EQUAL(15120, largest_series_product("0123456789", 5));
}

void test_can_get_the_largest_product_of_a_big_number(void) {
  TEST_ASSERT_EQUAL(
      23520, largest_series_product(
                 "73167176531330624919225119674426574742355349194934", 6));
}

void test_can_get_the_largest_product_of_a_big_number_ii(void) {
  TEST_ASSERT_EQUAL(
      28350, largest_series_product(
                 "52677741234314237566414902593461595376319419139427", 6));
}

void test_can_get_the_largest_product_of_a_big_number_project_euler(void) {
  TEST_ASSERT_EQUAL_INT64(
      23514624000,
      largest_series_product(
          "73167176531330624919225119674426574742355349194934969835203127745063"
          "26239578318016984801869478851843858615607891129494954595017379583319"
          "52853208805511125406987471585238630507156932909632952274430435576689"
          "66489504452445231617318564030987111217223831136222989342338030813533"
          "62766142828064444866452387493035890729629049156044077239071381051585"
          "93079608667017242712188399879790879227492190169972088809377665727333"
          "00105336788122023542180975125454059475224352584907711670556013604839"
          "58644670632441572215539753697817977846174064955149290862569321978468"
          "62248283972241375657056057490261407972968652414535100474821663704844"
          "03199890008895243450658541227588666881164271714799244429282308634656"
          "74813919123162824586178664583591245665294765456828489128831426076900"
          "42242190226710556263211111093705442175069416589604080719840385096245"
          "54443629812309878799272442849091888458015616609791913387549920052406"
          "36899125607176060588611646710940507754100225698315520005593572972571"
          "636269561882670428252483600823257530420752963450",
          13));
}

void test_reports_zero_if_the_only_digits_are_zero(void) {
  TEST_ASSERT_EQUAL(0, largest_series_product("0000", 2));
}

void test_reports_zero_if_all_spans_include_zero(void) {
  TEST_ASSERT_EQUAL(0, largest_series_product("99099", 3));
}

void test_rejects_span_longer_than_string_length(void) {
  TEST_ASSERT_EQUAL(-1, largest_series_product("123", 4));
}

void test_reports_1_for_empty_string_and_empty_product_(void) {
  TEST_ASSERT_EQUAL(1, largest_series_product("", 0));
}

void test_reports_1_for_nonempty_string_and_empty_product_(void) {
  TEST_ASSERT_EQUAL(1, largest_series_product("123", 0));
}

void test_rejects_empty_string_and_nonzero_span(void) {
  TEST_ASSERT_EQUAL(-1, largest_series_product("", 1));
}

void test_rejects_invalid_character_in_digits(void) {
  TEST_ASSERT_EQUAL(-1, largest_series_product("123a5", 2));
}

int main(void) {
  UnityBegin("largest_series_product.c");

  RUN_TEST(test_can_find_the_largest_product_of_2_with_numbers_in_order);
  RUN_TEST(test_can_find_the_largest_product_of_2);
  RUN_TEST(test_finds_the_largest_product_if_span_equals_length);
  RUN_TEST(test_can_find_the_largest_product_of_3_with_numbers_in_order);
  RUN_TEST(test_can_find_the_largest_product_of_3);
  RUN_TEST(test_can_find_the_largest_product_of_5_with_numbers_in_order);
  RUN_TEST(test_can_get_the_largest_product_of_a_big_number);
  RUN_TEST(test_can_get_the_largest_product_of_a_big_number_ii);
  RUN_TEST(test_can_get_the_largest_product_of_a_big_number_project_euler);
  RUN_TEST(test_reports_zero_if_the_only_digits_are_zero);
  RUN_TEST(test_reports_zero_if_all_spans_include_zero);
  RUN_TEST(test_rejects_span_longer_than_string_length);
  RUN_TEST(test_reports_1_for_empty_string_and_empty_product_);
  RUN_TEST(test_reports_1_for_nonempty_string_and_empty_product_);
  RUN_TEST(test_rejects_empty_string_and_nonzero_span);
  RUN_TEST(test_rejects_invalid_character_in_digits);

  UnityEnd();
  return 0;
}
