#lang racket

(provide perfect-numbers)

(define (divisors n)
  (filter
    (lambda (d) (= 0 (modulo n d)))
    (range 1 n)))

(define (is-perfect n)
  (= n (foldl + 0 (divisors n))))

(define (perfect-numbers n)
  (filter is-perfect (range 1 (+ 1 n))))
