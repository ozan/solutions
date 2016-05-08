#lang racket/base

(require "nucleotide-count.rkt")

(module+ test
  (require rackunit rackunit/text-ui)

  (define suite
    (test-suite
     "nucleotide count tests"

     (test-equal? "empty dna strand has no nucleotides"
                  (nucleotide-counts "")
                  '((#\A . 0) (#\C . 0) (#\G . 0) (#\T . 0)))

     (test-equal? "repetitive sequence has only guanine"
                  (nucleotide-counts "GGGGGGGG")
                  '((#\A . 0) (#\C . 0) (#\G . 8) (#\T . 0)))

     (test-equal? "counts all nucleotides"
                  (nucleotide-counts
                   "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
                  '((#\A . 20) (#\C . 12) (#\G . 17) (#\T . 21)))

     (test-exn "invalid nucleotide" exn:fail? (lambda () (nucleotide-counts "AGGTCCXGA")))))

  (run-tests suite))
