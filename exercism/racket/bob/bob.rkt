#lang racket

(require srfi/13/string racket/list)

(provide response-for)

(define (question? q)
  (string-suffix? "?" q))

(define (yelling? q)
  (and
    (string=? q (string-upcase q))
    (not (string=? q (string-downcase q)))))

(define (silence? q)
  (string=? "" (string-trim q)))

(define (response-for q)
  (cond
    ((silence? q) "Fine. Be that way!")
    ((yelling? q) "Whoa, chill out!")
    ((question? q) "Sure.")
    (else "Whatever.")))
