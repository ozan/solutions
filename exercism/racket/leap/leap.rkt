#lang racket

(provide leap-year?)

(define (divs n d) (= 0 (modulo n d)))

(define (leap-year? year)
  (or (divs year 400)
      (and (divs year 4)
           (not (divs year 100)))))
