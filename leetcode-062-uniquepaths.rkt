#!/usr/bin/env racket --script

(define (ones n)
  (map (lambda (_) 1) (range n)))

(define (add-top-and-left y xs)
  (cons (+ (car xs) y) xs))

(define (next-row _ prior)
  (foldr add-top-and-left (list 0) prior))

(define (unique-paths width height)
  (car (foldr next-row (ones (+ 1 width)) (range height))))


(write (unique-paths 3 4))  ; 35
