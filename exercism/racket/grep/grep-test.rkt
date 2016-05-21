#lang racket

(require "grep.rkt")

(module+ test
  (require rackunit rackunit/text-ui)

  (define-syntax-rule (grep-this-file pat-str)
    (grep-file "./grep-test.rkt" (regexp pat-str)))

  (define suite
    (test-suite "grep tests"

     (test-equal? "no-matches"
                  (grep-this-file "^#!/usr/bin/env perl")
                  '())

     (test-equal? "one match"
                  (grep-this-file "^#lang racket$")
                  '((1 . "#lang racket")))

     (test-equal? "a few matches"
                  (map car (grep-this-file "require .*"))
                  '(3 6 23))

     (test-equal? "many matches"
                  (+ 1
                     (length (grep-this-file "\\("))
                     (length (grep-this-file "^$")))
                  (length (file->lines "grep-test.rkt")))))

  (run-tests suite))
