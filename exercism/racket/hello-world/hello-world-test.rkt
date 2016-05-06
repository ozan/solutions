#lang racket

(require "hello-world.rkt")

(module+ test
  (require rackunit rackunit/text-ui)

  (define suite
    (test-suite
     "hello world tests"

     (test-equal? "no arg returns Hello, World!" (hello) "Hello, World!")
     (test-equal? "with arg returns Hello, arg!" (hello "exercism") "Hello, exercism!")))

  (run-tests suite))
