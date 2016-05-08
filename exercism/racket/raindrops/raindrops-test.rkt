#lang racket/base

(require "raindrops.rkt")

(module+ test
  (require rackunit rackunit/text-ui)

  (define suite
    (test-suite
     "raindrops tests"

     (test-equal? "test-1" (convert 1) "1")
     (test-equal? "test-3" (convert 3) "Pling")
     (test-equal? "test-5" (convert 5) "Plang")
     (test-equal? "test-7" (convert 7) "Plong")
     (test-equal? "test-6" (convert 6) "Pling")
     (test-equal? "test-9" (convert 9) "Pling")
     (test-equal? "test-10" (convert 10) "Plang")
     (test-equal? "test-15" (convert 15) "PlingPlang")
     (test-equal? "test-21" (convert 21) "PlingPlong")
     (test-equal? "test-25" (convert 25) "Plang")
     (test-equal? "test-35" (convert 35) "PlangPlong")
     (test-equal? "test-49" (convert 49) "Plong")
     (test-equal? "test-52" (convert 52) "52")
     (test-equal? "test-105" (convert 105) "PlingPlangPlong")
     (test-equal? "test-12121" (convert 12121) "12121")))

  (run-tests suite))
