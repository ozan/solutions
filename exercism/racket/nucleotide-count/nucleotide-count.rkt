#lang racket

(provide nucleotide-counts)

(define (nucleotide-counts strand)
  (let ([counts (make-hash '((#\A . 0) (#\C . 0) (#\G . 0) (#\T . 0)))])
    (for ([nuc (string->list strand)])
      (hash-set! counts nuc (+ 1 (hash-ref counts nuc))))
    (sort (hash->list counts) #:key car char<?)))
