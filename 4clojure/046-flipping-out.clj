#!/usr/bin/env lein-exec

; Write a higher-order function which flips the order of the arguments of an
; input function.

(defn flip [f]
  (fn [a b]
    (f b a)))

(assert (= [1 2 3] ((flip take) [1 2 3 4 5] 3)))
