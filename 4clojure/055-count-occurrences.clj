#!/usr/bin/env lein-exec

; Write a function which returns a map containing the number of
; occurences of each distinct item in a sequence.

(defn freqs [xs]
 (let [parts (partition-by identity (sort xs))]
  (into {} (map
            vector
            (map #(first %) parts)
            (map #(count %) parts)))))


(assert (= (freqs [1 1 2 3 2 1 1]) {1 4, 2 2, 3 1}))
(assert (= (freqs [:b :a :b :a :b]) {:a 2, :b 3}))
(assert (= (freqs '([1 2] [1 3] [1 3])) {[1 2] 1, [1 3] 2}))
