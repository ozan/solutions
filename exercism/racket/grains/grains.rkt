#lang racket

(provide square total)

(define (square n) (expt 2 (- n 1)))

(define (total) (- (square 65) 1))
