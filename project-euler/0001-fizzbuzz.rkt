#!/usr/bin/env racket --script

(define (divisible-by n div)
  (= 0 (modulo n div)))

(define (sum-multiples a b upto)
  (apply + (filter (lambda (n) (or (divisible-by n a)
                                   (divisible-by n b)))
            (range 0 upto))))

(write (sum-multiples 3 5 1000) )
