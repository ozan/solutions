#!/usr/bin/env lein-exec

; Create a function which takes an integer and a nested collection of
; integers as arguments. Analyze the elements of the input collection
; and return a sequence which maintains the nested structure, and which
; includes all elements starting from the head whose sum is less than or
; equal to the input integer.

(defn sequs [sum [x & xs]]
  (if (nil? x) []
    (if (sequential? x)
      (concat [(sequs sum x)] (sequs (- sum (reduce + (flatten x))) xs))
      (if (< sum x)
        []
        (concat [x] (sequs (- sum x) xs))))))


(assert (=  (sequs 10 [1 2 [3 [4 5] 6] 7])
   '(1 2 (3 (4)))))
(assert (=  (sequs 30 [1 2 [3 [4 [5 [6 [7 8]] 9]] 10] 11])
   '(1 2 (3 (4 (5 (6 (7))))))))
(assert (=  (sequs 9 (range))
   '(0 1 2 3)))
(assert (=  (sequs 1 [[[[[1]]]]])
   '(((((1)))))))
(assert (=  (sequs 0 [1 2 [3 [4 5] 6] 7])
   '()))
(assert (=  (sequs 0 [0 0 [0 [0]]])
   '(0 0 (0 (0)))))
(assert (=  (sequs 1 [-10 [1 [2 3 [4 5 [6 7 [8]]]]]])
   '(-10 (1 (2 3 (4))))))
