#!/usr/bin/env lein-exec


(defn ones [n]
  (take n (repeat 1)))

(defn add-top-and-left [xs y]
  (concat xs [(+ (last xs) y)]))

(defn next-row [prior _]
  (rest (reduce add-top-and-left [0] prior)))

(defn unique-paths [width height]
  (last (reduce next-row (ones (+ 1 width)) (range height))))


(println (unique-paths 3 4))  ;; 35
