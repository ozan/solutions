#lang racket

(require "etl.rkt")

(module+ test
  (require rackunit rackunit/text-ui)

  (define mixed-case-input (hash 1 '("a" "E" "I" "o" "U" "L" "N" "r" "s" "T")
                                 2 '("D" "G")
                                 3 '("B" "c" "M" "P")
                                 4 '("f" "h" "V" "W" "y")
                                 5 '("K")
                                 8 '("J" "x")
                                 10 '("q" "z")))

  (define expected (hash "a" 1 "b" 3 "c" 3 "d" 2 "e" 1 "f" 4 "g" 2
                         "h" 4 "i" 1 "j" 8 "k" 5 "l" 1 "m" 3 "n" 1
                         "o" 1 "p" 3 "q" 10 "r" 1 "s" 1 "t" 1
                         "u" 1 "v" 4 "x" 8 "w" 4 "y" 4 "z" 10))

  (define negative-keys-input (hash 1 '("L" "N")
                                    -3 '("B" "c" "P")))

  (define listof-chars-input (hash 1 '(#\N #\r #\q)))

  (define suite
    (test-suite
     "etl tests"

     (test-true "empty hash"
                (zero? (hash-count (etl (make-hash)))))

     (test-case
      "mixed case input"
      (define actual (etl mixed-case-input))
      (check-equal? (hash-count actual) (hash-count expected))
      (for ([k (hash-keys actual)])
        #;(printf "actual: ~a -> ~a, expected: ~a -> ~a\n"
                  k (hash-ref actual k)
                  k (hash-ref expected k))
        (check-equal? (hash-ref actual k)
                      (hash-ref expected k))))

     (test-exn
      "test bad input: negative keys"
      exn:fail:contract? (lambda () (etl negative-keys-input)))

     (test-exn
      "test bad input: list of non-string values"
      exn:fail:contract? (lambda () (etl listof-chars-input)))))

  (run-tests suite))
