#!/usr/bin/env lein-exec

; Given a vector of integers, find the longest consecutive sub-sequence
; of increasing numbers. If two sub-sequences have the same length, use
; the one that occurs first. An increasing sub-sequence must have a
; length of 2 or greater to qualify.

(defn longest-subseq [xs]
  (loop [i 0
         j 1
         si 0
         sj 1
         max-i 0
         max-j 1]
    (if (= j (count xs))
      (if (> (- max-j max-i) 1) (subvec xs max-i max-j) [])
      (if (> (xs j) (xs i))
        (recur (inc i) (inc j) si (inc sj) (if (> (- (inc sj) si) (- max-j max-i)) si max-i) (if (> (- (inc sj) si) (- max-j max-i)) (inc sj) max-j))
        (recur (inc i) (inc j) sj (inc sj) max-i max-j)))))


(assert (= (longest-subseq [1 0 1 2 3 0 4 5]) [0 1 2 3]))
(assert (= (longest-subseq [5 6 1 3 2 7]) [5 6]))
(assert (= (longest-subseq [2 3 3 4 5]) [3 4 5]))
(assert (= (longest-subseq [7 6 5 4]) []))
