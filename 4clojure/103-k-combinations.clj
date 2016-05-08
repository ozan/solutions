#!/usr/bin/env lein-exec

; Given a sequence S consisting of n elements generate all
; k-combinations of S, i. e. generate all possible sets consisting of k
; distinct elements taken from S. The number of k-combinations for a
; sequence is equal to the binomial coefficient.

(defn k-combinations [n s]
  (if (> n (count s)) #{}
    (if (= 1 n) (into #{} (map (comp set vector) s))
      (let [prior (k-combinations (dec n) s)]
        (into #{} (for [p prior
              q (clojure.set/difference s p)]
          (clojure.set/union p #{q})
          ))))))


(assert (= (k-combinations 1 #{4 5 6}) #{#{4} #{5} #{6}}))
(assert (= (k-combinations 10 #{4 5 6}) #{}))
(assert (= (k-combinations 2 #{0 1 2}) #{#{0 1} #{0 2} #{1 2}}))
(assert (= (k-combinations 3 #{0 1 2 3 4}) #{#{0 1 2} #{0 1 3} #{0 1 4} #{0 2 3} #{0 2 4}
                         #{0 3 4} #{1 2 3} #{1 2 4} #{1 3 4} #{2 3 4}}))
(assert (= (k-combinations 4 #{[1 2 3] :a "abc" "efg"}) #{#{[1 2 3] :a "abc" "efg"}}))
(assert (= (k-combinations 2 #{[1 2 3] :a "abc" "efg"}) #{#{[1 2 3] :a} #{[1 2 3] "abc"} #{[1 2 3] "efg"}
                                    #{:a "abc"} #{:a "efg"} #{"abc" "efg"}}))

