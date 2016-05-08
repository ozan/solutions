#lang racket

(require "roman-numerals.rkt")

(module+ test
  (require rackunit rackunit/text-ui)

  (define suite
    (test-suite
     "Roman Numeral tests"

     (test-equal? "1"
                  (to-roman 1)
                  "I")

     (test-equal? "2"
                  (to-roman 2)
                  "II")

     (test-equal? "3"
                  (to-roman 3)
                  "III")

     (test-equal? "4"
                  (to-roman 4)
                  "IV")

     (test-equal? "5"
                  (to-roman 5)
                  "V")

     (test-equal? "6"
                  (to-roman 6)
                  "VI")

     (test-equal? "9"
                  (to-roman 9)
                  "IX")

     (test-equal? "27"
                  (to-roman 27)
                  "XXVII")

     (test-equal? "48"
                  (to-roman 48)
                  "XLVIII")

     (test-equal? "59"
                  (to-roman 59)
                  "LIX")

     (test-equal? "93"
                  (to-roman 93)
                  "XCIII")

     (test-equal? "141"
                  (to-roman 141)
                  "CXLI")

     (test-equal? "163"
                  (to-roman 163)
                  "CLXIII")

     (test-equal? "402"
                  (to-roman 402)
                  "CDII")

     (test-equal? "575"
                  (to-roman 575)
                  "DLXXV")

     (test-equal? "911"
                  (to-roman 911)
                  "CMXI")

     (test-equal? "1024"
                  (to-roman 1024)
                  "MXXIV")

     (test-equal? "3000"
                  (to-roman 3000)
                  "MMM")
     ))

  (run-tests suite))