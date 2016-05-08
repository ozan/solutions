#lang racket/base

(require "phone-number.rkt")

(module+ test
  (require rackunit rackunit/text-ui)

  (define suite
    (test-suite
     "phone number tests"

     (test-equal? "cleans number" (numbers "(123) 456-7890") "1234567890")
     (test-equal? "cleans numbers with dots" (numbers "123.456.7890") "1234567890")
     (test-equal? "valid when 11 digits and first is 1" (numbers "11234567890") "1234567890")
     (test-equal? "invalid when 11 digits" (numbers "21234567890") "0000000000")
     (test-equal? "invalid when 9 digits" (numbers "123456789") "0000000000")
     (test-equal? "area code" (area-code "1234567890") "123")
     (test-equal? "pprint" (pprint "1234567890") "(123) 456-7890")
     (test-equal? "pprint with full us phone number" (pprint "11234567890") "(123) 456-7890")))

  (run-tests suite))
