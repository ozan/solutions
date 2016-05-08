#!/usr/bin/env lein-exec

; Write a function which returns a sequence of lists of x items each.
; Lists of less than x items should not be returned.

(defn part [n xs]
  (cons
   (take n xs)
   (let [the-others (drop n xs)]
     (if (<= n (count the-others))
       (part n the-others)
       ()))))


(assert (= (part 3 (range 9)) '((0 1 2) (3 4 5) (6 7 8))))
(assert (= (part 2 (range 8)) '((0 1) (2 3) (4 5) (6 7))))
(assert (= (part 3 (range 8)) '((0 1 2) (3 4 5))))
