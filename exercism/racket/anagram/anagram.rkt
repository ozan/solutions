#lang racket

(provide anagrams-for)

(define (string-sort word)
  (list->string (sort (string->list word) char<?)))

(define (key word)
  (string-sort (string-downcase word)))

(define (anagram a b)
  (string=? (key a) (key b)))

(define (case-equiv a b)
  (string=? (string-downcase a) (string-downcase b)))

(define (anagrams-for word choices)
  (filter (λ (choice) (and (anagram word choice) (not (case-equiv word choice))))
          choices))
