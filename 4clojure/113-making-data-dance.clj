#!/usr/bin/env lein-exec

; Write a function that takes a variable number of integer arguments. If
; the output is coerced into a string, it should return a comma (and
; space) separated list of the inputs sorted smallest to largest. If the
; output is coerced into a sequence, it should return a seq of unique
; input elements in the same order as they were entered.

(defn formattable [& integers]
  (reify clojure.lang.Seqable
    (toString [this] (clojure.string/join ", " (map str (sort integers))))
    (seq [this] (if (empty? integers) nil (distinct integers)))))


(assert (= "1, 2, 3" (str (formattable 2 1 3))))
(assert (= '(2 1 3) (seq (formattable 2 1 3))))
(assert (= '(2 1 3) (seq (formattable 2 1 3 3 1 2))))
(assert (= '(1) (seq (apply formattable (repeat 5 1)))))
(assert (= "1, 1, 1, 1, 1" (str (apply formattable (repeat 5 1)))))
(assert (and (= nil (seq (formattable)))
     (=  "" (str (formattable)))))
