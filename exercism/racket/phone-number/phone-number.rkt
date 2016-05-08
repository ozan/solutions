#lang racket

(provide numbers area-code pprint)

(define (numbers str)
  (let ([clean (regexp-replace* #rx"[^0-9]" str "")])
    (if (or (= 10 (string-length clean))
            (and (= 11 (string-length clean))
                 (string-prefix? clean "1")))
        (list->string (take-right (string->list clean) 10))
        "0000000000")))

(define (area-code str)
  (substring str 0 3))

(define (pprint str)
  (let ([clean (numbers str)])
    (format "(~a) ~a-~a"
      (area-code clean)
      (substring clean 3 6)
      (substring clean 6 10))))
