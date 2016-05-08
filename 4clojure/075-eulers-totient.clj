#!/usr/bin/env lein-exec

; Two numbers are coprime if their greatest common divisor equals 1.
; Euler's totient function f(x) is defined as the number of positive
; integers less than x which are coprime to x. The special case f(1)
; equals 1. Write a function which calculates Euler's totient function.

(defn totient [n]
  (letfn [(gcd [a b] (if (= 0 b) a (gcd b (mod a b))))]
    (count (filter #(= 1 (gcd n %)) (range n)))))


(assert (= (totient 1) 1))
(assert (= (totient 10) (count '(1 3 7 9)) 4))
(assert (= (totient 40) 16))
(assert (= (totient 99) 60))
