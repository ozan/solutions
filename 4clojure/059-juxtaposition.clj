#!/usr/bin/env lein-exec

; Take a set of functions and return a new function that takes a
; variable number of arguments and returns a sequence containing the
; result of applying each function left-to-right to the argument list.

(defn my-juxt [& fs]
  (fn [& args]
    (map #(apply % args) fs)))


(assert (= [21 6 1] ((my-juxt + max min) 2 3 5 1 6 4)))
(assert (= ["HELLO" 5] ((my-juxt #(.toUpperCase %) count) "hello")))
(assert (= [2 6 4] ((my-juxt :a :c :b) {:a 2, :b 4, :c 6, :d 8 :e 10})))
