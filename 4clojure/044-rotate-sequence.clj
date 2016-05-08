#!/usr/bin/env lein-exec

; Write a function which can rotate a sequence in either direction.

(defn rotate [n xs]
     (let [n (mod n (count xs))]
       (concat (drop n xs) (take n xs))))


(assert (= (rotate 2 [1 2 3 4 5]) '(3 4 5 1 2)))
(assert (= (rotate -2 [1 2 3 4 5]) '(4 5 1 2 3)))
(assert (= (rotate 6 [1 2 3 4 5]) '(2 3 4 5 1)))
(assert (= (rotate 1 '(:a :b :c)) '(:b :c :a)))
(assert (= (rotate -4 '(:a :b :c)) '(:c :a :b)))
