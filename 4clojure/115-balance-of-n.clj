#!/usr/bin/env lein-exec

; A balanced number is one whose component digits have the same sum on
; the left and right halves of the number. Write a function which
; accepts an integer n, and returns true iff n is balanced.

(defn balanced? [x]
  (let [s (str x)
        l (count s)]
    (= (reduce + (map int (take (Math/ceil  (/ l 2)) s)))
       (reduce + (map int (drop (Math/floor (/ l 2)) s))))))


(assert (= true (balanced? 11)))
(assert (= true (balanced? 121)))
(assert (= false (balanced? 123)))
(assert (= true (balanced? 0)))
(assert (= false (balanced? 88099)))
(assert (= true (balanced? 89098)))
(assert (= true (balanced? 89089)))
(assert (= (take 20 (filter balanced? (range)))
   [0 1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 101]))
