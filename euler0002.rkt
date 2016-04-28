#!/usr/bin/env racket --script

(require srfi/41)

(define (fibgen a b) (stream-cons a (fibgen b (+ a b))))

(define fib (fibgen 0 1))

(define (fibsum upto)
  (apply +
    (stream->list
      (stream-take-while (lambda (n) (< n upto))
        (stream-filter even? fib)))))

(write (fibsum 4e6))
