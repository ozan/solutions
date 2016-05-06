#lang racket/base

(require "grains.rkt")

(module+ test
  (require rackunit rackunit/text-ui)

  (define suite
    (test-suite
     "grains tests"

     (test-eqv? "square 1" (square 1) 1)
     (test-eqv? "square 2" (square 2) 2)
     (test-eqv? "square 3" (square 3) 4)
     (test-eqv? "square 4" (square 4) 8)
     (test-eqv? "square 16" (square 16) 32768)
     (test-eqv? "square 32" (square 32) 2147483648)
     (test-eqv? "square 64" (square 64) 9223372036854775808)
     (test-eqv? "total grains" (total) 18446744073709551615)))

  (run-tests suite))
