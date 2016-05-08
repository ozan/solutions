#!/usr/bin/env lein-exec

; take-while is great for filtering sequences, but it limited: you can
; only examine a single item of the sequence at a time. What if you need
; to keep track of some state as you go over the sequence?

; Write a function which accepts an integer n, a predicate p, and a
; sequence. It should return a lazy sequence of items in the list up to,
; but not including, the nth item that satisfies the predicate.

(defn global-take-while [n p xs]
  (lazy-seq
   (if (p (first xs)) ; passes, so decrement n
     (if (> n 1)
       (cons (first xs) (global-take-while (dec n) p (rest xs)))) ; TODO: combine into 1
     (cons (first xs) (global-take-while n p (rest xs))))))


(assert (= [2 3 5 7 11 13]
   (global-take-while 4 #(= 2 (mod % 3))
         [2 3 5 7 11 13 17 19 23])))
(assert (= ["this" "is" "a" "sentence"]
   (global-take-while 3 #(some #{\i} %)
         ["this" "is" "a" "sentence" "i" "wrote"])))
(assert (= ["this" "is"]
   (global-take-while 1 #{"a"}
         ["this" "is" "a" "sentence" "i" "wrote"])))
