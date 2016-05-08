#!/usr/bin/env lein-exec

; Write a function that takes a sequence of integers and returns a
; sequence of "intervals". Each interval is a a vector of two integers,
; start and end, such that all integers between start and end
; (inclusive) are contained in the input sequence.

(defn intervals [xs]
  (->> xs
       sort
       (partition-all 2 1)
       (#(cons [(ffirst %)] %))
       (remove (fn [[a b]] (and a b (< (- b a) 2))))
       flatten
       (partition 2)
       ))


(assert (= (intervals [1 2 3]) [[1 3]]))
(assert (= (intervals [10 9 8 1 2 3]) [[1 3] [8 10]]))
(assert (= (intervals [1 1 1 1 1 1 1]) [[1 1]]))
(assert (= (intervals []) []))
(assert (= (intervals [19 4 17 1 3 10 2 13 13 2 16 4 2 15 13 9 6 14 2 11])
       [[1 4] [6 6] [9 11] [13 17] [19 19]]))
