#!/usr/bin/env lein-exec

; Given a pair of numbers, the start and end point, find a path between
; the two using only three possible operations: * double * halve (odd
; numbers cannot be halved) * add 2. Find the shortest path through the
; "maze". Because there are multiple shortest paths, you must return the
; length of the shortest path, not the path itself.

(defn steps [start end]
  (loop [[[n depth] & others] [[start 1]]
         seen #{}]
    (if (= n end) depth
      (recur (concat others
                     (->> [(* n 2) (+ n 2) (/ n 2)]
                          (filter integer?)
                          (remove seen)
                          (map #(vector % (inc depth)))))
             (conj seen #{n})))))


(assert (= 1 (steps 1 1)))  ; 1
(assert (= 3 (steps 3 12))) ; 3 6 12
(assert (= 3 (steps 12 3))) ; 12 6 3
(assert (= 3 (steps 5 9)))  ; 5 7 9
(assert (= 9 (steps 9 2)))  ; 9 18 20 10 12 6 8 4 2
(assert (= 5 (steps 9 12))) ; 9 11 22 24 12
