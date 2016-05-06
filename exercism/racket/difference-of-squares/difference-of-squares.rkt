#lang racket

(provide sum-of-squares square-of-sums difference)

(define (difference n)
  (- (square-of-sums n) (sum-of-squares n)))

(define (square-of-sums n)
  (sqr (sum (range (+ 1 n)))))

(define (sum-of-squares n)
  (sum (map sqr (range (+ 1 n)))))

(define (sum xs)
  (foldl + 0 xs))
