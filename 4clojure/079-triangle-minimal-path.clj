#!/usr/bin/env lein-exec

; Write a function which calculates the sum of the minimal path through
; a triangle. The triangle is represented as a collection of vectors.
; The path should start at the top of the triangle and move to an
; adjacent number on the next row until the bottom of the triangle is
; reached.

(defn minimal-path [triangle]
   (letfn [(next-row [prior subsequent]
             (let [pairs (partition 2 1 prior)
                   best (map (partial apply min) pairs)
                   all-prior (concat [(first prior)] best [(last prior)])]
               (mapcat (comp vector +) all-prior subsequent)))]
     (apply min (reduce next-row triangle))))


(assert (= 7 (minimal-path '([1]
                            [2 4]
                           [5 1 4]
                          [2 3 4 5])))) ; 1->2->1->3

(assert (= 20 (minimal-path '([3]
                             [2 4]
                            [1 9 3]
                           [9 9 2 4]
                          [4 6 6 7 8]
                         [5 7 3 5 1 4])))) ; 3->4->3->2->7->1
