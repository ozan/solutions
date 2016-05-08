#!/usr/bin/env lein-exec

; Write a function that takes a two-argument predicate, a value, and a
; collectionand returns a new collection where the value is inserted
; between every two items that satisfy the predicate.

(defn insert-between [predicate delimiter xs]
  (mapcat (fn [[a b]] (if (and (not (nil? b)) (predicate a b)) (list a delimiter) (list a)))
          (partition-all 2 1 xs)))


(assert (= '(1 :less 6 :less 7 4 3) (insert-between < :less [1 6 7 4 3])))
(assert (= '(2) (insert-between > :more [2])))
(assert (= [0 1 :x 2 :x 3 :x 4]  (insert-between #(and (pos? %) (< % %2)) :x (range 5))))
(assert (empty? (insert-between > :more ())))
(assert (= [0 1 :same 1 2 3 :same 5 8 13 :same 21]
   (take 12 (->> [0 1]
                 (iterate (fn [[a b]] [b (+ a b)]))
                 (map first) ; fibonacci numbers
                 (insert-between (fn [a b] ; both even or both odd
                       (= (mod a 2) (mod b 2)))
                     :same)))))
