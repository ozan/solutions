#!/usr/bin/env lein-exec

; Given a variable number of sets of integers, create a function which
; returns true iff all of the sets have a non-empty subset with an
; equivalent summation.

(defn have-subset? [& sets]
  (let [powerset (fn [s] (reduce
                           #(clojure.set/union %1 (into #{} (for [subset %1] (conj subset %2))))
                           #{#{}}
                           s))
        sumset (fn [s] (into #{} (map (partial reduce +) s)))]
    (->> sets
         (map powerset)
         (map #(remove empty? %))
         (map sumset)
         (apply clojure.set/intersection)
         empty?
         not)))


(assert (= true  (have-subset? #{-1 1 99}
             #{-2 2 888}
             #{-3 3 7777}))) ; ex. all sets have a subset which sums to zero
(assert (= false (have-subset? #{1}
             #{2}
             #{3}
             #{4})))
(assert (= true  (have-subset? #{1})))
(assert (= false (have-subset? #{1 -3 51 9}
             #{0}
             #{9 2 81 33})))
(assert (= true  (have-subset? #{1 3 5}
             #{9 11 4}
             #{-3 12 3}
             #{-3 4 -2 10})))
(assert (= false (have-subset? #{-1 -2 -3 -4 -5 -6}
             #{1 2 3 4 5 6 7 8 9})))
(assert (= true  (have-subset? #{1 3 5 7}
             #{2 4 6 8})))
(assert (= true  (have-subset? #{-1 3 -5 7 -9 11 -13 15}
             #{1 -3 5 -7 9 -11 13 -15}
             #{1 -1 2 -2 4 -4 8 -8})))
(assert (= true  (have-subset? #{-10 9 -8 7 -6 5 -4 3 -2 1}
             #{10 -9 8 -7 6 -5 4 -3 2 -1})))
