#!/usr/bin/env lein-exec

; Write a function which returns a sequence of digits of a non-negative
; number (first argument) in numerical system with an arbitrary base
; (second argument). Digits should be represented with their integer
; values, e.g. 15 would be [1 5] in base 10, [1 1 1 1] in base 2 and
; [15] in base 16.


(defn digits [n base]
  (if (>= n base)
    (concat (digits (int (/ n base)) base) [(mod n base)])
    [n]))


(assert (= [1 2 3 4 5 0 1] (digits 1234501 10)))
(assert (= [0] (digits 0 11)))
(assert (= [1 0 0 1] (digits 9 2)))
(assert (= [1 0] (let [n (rand-int 100000)](digits n n))))
(assert (= [16 18 5 24 15 1] (digits Integer/MAX_VALUE 42)))
