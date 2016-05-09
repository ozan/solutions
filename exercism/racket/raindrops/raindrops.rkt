#lang racket

(provide convert)

(define (divides n k)
  (= 0 (modulo n k)))

(define (convert n)
  (let ([div3 (if (divides n 3) "Pling" "")]
        [div5 (if (divides n 5) "Plang" "")]
        [div7 (if (divides n 7) "Plong" "")])
    (if (string=? "" (string-append div3 div5 div7))
        (format "~a" n)
        (format "~a~a~a" div3 div5 div7))))
