#!/usr/bin/env lein-exec

; Write a function which flattens any nested combination of sequential
; things (lists, vectors, etc.), but maintains the lowest level
; sequential items. The result should be a sequence of sequences with
; only one level of nesting.

(defn partially-flatten [xs]
  (if (every? sequential? xs)
    (mapcat partially-flatten xs)
    [xs]))


(assert (= (partially-flatten [["Do"] ["Nothing"]])
   [["Do"] ["Nothing"]]))
(assert (= (partially-flatten [[[[:a :b]]] [[:c :d]] [:e :f]])
   [[:a :b] [:c :d] [:e :f]]))
(assert (= (partially-flatten '((1 2)((3 4)((((5 6)))))))
   '((1 2)(3 4)(5 6))))
