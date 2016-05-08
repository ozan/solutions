#!/usr/bin/env lein-exec

; Write a function which generates the power set of a given set. The
; power set of a set x is the set of all subsets of x, including the
; empty set and x itself.


(defn power-set [s]
   (reduce
    #(clojure.set/union %1 (into #{} (for [subset %1] (conj subset %2))))
    #{#{}}
    s))


(assert (= (power-set #{1 :a}) #{#{1 :a} #{:a} #{} #{1}}))

(assert (= (power-set #{}) #{#{}}))

(assert (= (power-set #{1 2 3})
   #{#{} #{1} #{2} #{3} #{1 2} #{1 3} #{2 3} #{1 2 3}}))

(assert (= (count (power-set (into #{} (range 10)))) 1024))
