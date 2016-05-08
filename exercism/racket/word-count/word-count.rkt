#lang racket

(provide word-count)

(define (count-occurences key count-hash)
  (let ([current-count (hash-ref count-hash key 0)])
    (hash-set! count-hash key (+ 1 current-count))
    count-hash))

(define (word-count sentence)
  (foldl count-occurences (make-hash) (regexp-split #rx"[ \n]+" sentence)))
