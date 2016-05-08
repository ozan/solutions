#!/usr/bin/env lein-exec

; Write a function that returns a lazy sequence of "pronunciations" of a
; sequence of numbers. A pronunciation of each element in the sequence
; consists of the number of repeating identical numbers and the number
; itself. For example, [1 1] is pronounced as [2 1] ("two ones"), which
; in turn is pronounced as [1 2 1 1] ("one two, one one").

; Your function should accept an initial sequence of numbers, and return
; an infinite lazy sequence of pronunciations, each element being a
; pronunciation of the previous element.


(defn pronounce-seq [xs]
   (lazy-seq
    (let [pron (->> xs
                    (partition-by identity)
                    (map #(vector (count %) (first %)))
                    (reduce concat))]
      (cons pron (pronounce-seq pron)))))


(assert (= [[1 1] [2 1] [1 2 1 1]] (take 3 (pronounce-seq [1]))))
(assert (= [3 1 2 4] (first (pronounce-seq [1 1 1 4 4]))))
(assert (= [1 1 1 3 2 1 3 2 1 1] (nth (pronounce-seq [1]) 6)))
(assert (= 338 (count (nth (pronounce-seq [3 2]) 15))))
