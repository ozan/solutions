#lang racket

(provide etl)

(define (etl h)
  (if
    (> (count (curry > 0) (hash-keys h)) 0)
    (raise (exn:fail))
    (for*/hash ([(k vals) (in-hash h)]
                [v (in-list vals)])
      (values (string-downcase v) k))))
