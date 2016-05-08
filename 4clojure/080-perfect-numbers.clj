#!/usr/bin/env lein-exec

; A number is "perfect" if the sum of its divisors equal the number
; itself. 6 is a perfect number because 1+2+3=6. Write a function which
; returns true for perfect numbers and false otherwise.

(defn perfect? [n]
 (= n (reduce + (remove nil?
                 (for [i (range 1 n)]
                  (if (= 0 (mod n i)) i))))))


(assert (= (perfect? 6) true))
(assert (= (perfect? 7) false))
(assert (= (perfect? 496) true))
(assert (= (perfect? 500) false))
(assert (= (perfect? 8128) true))
