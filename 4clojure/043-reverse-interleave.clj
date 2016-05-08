#!/usr/bin/env lein-exec

; Write a function which reverses the interleave process into x number
; of subsequences.

(defn reverse-interleave [xs n]
  (apply map vector (partition n xs)))


(assert (= (reverse-interleave [1 2 3 4 5 6] 2) '((1 3 5) (2 4 6))))
(assert (= (reverse-interleave (range 9) 3) '((0 3 6) (1 4 7) (2 5 8))))
(assert (= (reverse-interleave (range 10) 5) '((0 5) (1 6) (2 7) (3 8) (4 9))))
