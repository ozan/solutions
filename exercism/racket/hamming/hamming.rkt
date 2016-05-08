#lang racket

(provide hamming-distance)

(define (hamming-distance x-str y-str)
  (let ([xs (string->list x-str)]
        [ys (string->list y-str)])
    (count (negate equal?) xs ys)))
