#!/usr/bin/env racket --script

(define (int-vals s)
  (map char->integer (string->list s)))

(define (anagrams words)
  (group-by (lambda (s) (sort (int-vals s) <)) words))

(write (anagrams '("veer" "lake" "item" "kale" "mite" "ever")))
