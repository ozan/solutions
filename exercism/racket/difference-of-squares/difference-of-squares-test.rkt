#lang racket/base

(require "difference-of-squares.rkt")

(module+ test
  (require rackunit rackunit/text-ui)

  (define suite
    (test-suite
     "difference of squares"

     (test-eqv? "square-of-sums-to-5" (square-of-sums 5) 225)
     (test-eqv? "sum-of-squares-to-5" (sum-of-squares 5) 55)
     (test-eqv? "difference of-sums-to-5" (difference 5) 170)
     (test-eqv? "square-of-sums-to-10" (square-of-sums 10) 3025)
     (test-eqv? "sum-of-squares-to-10"  (sum-of-squares 10) 385)
     (test-eqv? "difference of-sums-to-10" (difference 10) 2640)
     (test-eqv? "square-of-sums-to-100" (square-of-sums 100) 25502500)
     (test-eqv? "sum-of-squares-to-100" (sum-of-squares 100) 338350)
     (test-eqv? "difference of-sums-to-100" (difference 100) 25164150)))

  (run-tests suite))
