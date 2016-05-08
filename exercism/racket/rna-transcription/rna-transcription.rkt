#lang racket

(provide to-rna)

(define h #hash((#\C . #\G) (#\G . #\C) (#\A . #\U) (#\T . #\A)))

(define dna->rna (curry hash-ref h))

(define (to-rna dna)
  (list->string (map dna->rna (string->list dna))))
