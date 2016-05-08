#!/usr/bin/env lein-exec

; Given an input sequence of keywords and numbers, create a map such
; that each key in the map is a keyword, and the value is a sequence of
; all the numbers (if any) between it and the next keyword in the
; sequence.


(defn keys-vals [xs]
  (let [partitioned (partition-by #(and (keyword? %) (identity %)) xs)
        pairs (map vector partitioned (rest partitioned))
        relevant-pairs (filter #(->> % first first keyword?) pairs)]
    (into {}
          (for [[k v] relevant-pairs]
            (if (keyword? (first v))
              [(first k) []]
              [(first k) (into [] v)])))))


(assert (= {} (keys-vals [])))
(assert (= {:a [1]} (keys-vals [:a 1])))
(assert (= {:a [1], :b [2]} (keys-vals [:a 1, :b 2])))
(assert (= {:a [1 2 3], :b [], :c [4]} (keys-vals [:a 1 2 3 :b :c 4])))
