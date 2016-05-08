#lang racket

(provide to-roman)

(define parts
  '((1000 "M")
    (900 "CM")
    (500 "D")
    (400 "CD")
    (100 "C")
    (90 "XC")
    (50 "L")
    (49 "IL")
    (40 "XL")
    (10 "X")
    (9 "IX")
    (5 "V")
    (4 "IV")
    (1 "I")))

(define (to-roman n)
  (if (= 0 n) (string)
    (let ([part (car (filter (lambda (p) (<= (car p) n)) parts))])
      (string-append
        (cadr part)
        (to-roman (- n (car part)))))))
