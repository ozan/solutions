#!/usr/bin/env lein-exec

; Create a function which accepts as input a boolean algebra function in
; the form of a set of sets, where the inner sets are collections of
; symbols corresponding to the input boolean variables which satisfy the
; function (the inputs of the inner sets are conjoint, and the sets
; themselves are disjoint... also known as canonical minterms). Note:
; capitalized symbols represent truth, and lower-case symbols represent
; negation of the inputs. Your function must return the minimal function
; which is logically equivalent to the input.

(defn veitch [bafs]
  (let [sym-diff (fn [a b]
                   (clojure.set/union
                     (clojure.set/difference a b)
                     (clojure.set/difference b a)))
        complementary? (fn [a b]
                         (->> (sym-diff a b)
                              (map #(clojure.string/capitalize %))
                              distinct
                              count
                              (= 1)))
        simplify (fn [bafs residue]
                   (let [simplification (for [a bafs b (disj bafs a) :when (complementary? a b)]
                                          [(clojure.set/intersection a b) a b])
                         to-remove (set (mapcat rest simplification))
                         more-residue (clojure.set/difference bafs to-remove)
                         to-simplify (set (map first simplification))]
                     (if (= bafs to-simplify) residue
                       (recur to-simplify (clojure.set/union residue more-residue)))))
        simpflified (simplify bafs #{})
        reapplied (map (fn [s] (filter #(clojure.set/subset? % s) simpflified)) bafs)
        ]
    (set (map first (filter #(= (count %) 1) reapplied)))))


(assert (= (veitch #{#{'a 'B 'C 'd}
                     #{'A 'b 'c 'd}
                     #{'A 'b 'c 'D}
                     #{'A 'b 'C 'd}
                     #{'A 'b 'C 'D}
                     #{'A 'B 'c 'd}
                     #{'A 'B 'c 'D}
                     #{'A 'B 'C 'd}})
   #{#{'A 'c}
     #{'A 'b}
     #{'B 'C 'd}}))

(assert (= (veitch #{#{'A 'B 'C 'D}
         #{'A 'B 'C 'd}})
   #{#{'A 'B 'C}}))

(assert (= (veitch #{#{'a 'b 'c 'd}
                     #{'a 'B 'c 'd}
                     #{'a 'b 'c 'D}
                     #{'a 'B 'c 'D}
                     #{'A 'B 'C 'd}
                     #{'A 'B 'C 'D}
                     #{'A 'b 'C 'd}
                     #{'A 'b 'C 'D}})
   #{#{'a 'c}
     #{'A 'C}}))

(assert (= (veitch #{#{'a 'b 'c}
                     #{'a 'B 'c}
                     #{'a 'b 'C}
                     #{'a 'B 'C}})
   #{#{'a}}))

(assert (= (veitch #{#{'a 'B 'c 'd}
                     #{'A 'B 'c 'D}
                     #{'A 'b 'C 'D}
                     #{'a 'b 'c 'D}
                     #{'a 'B 'C 'D}
                     #{'A 'B 'C 'd}})
   #{#{'a 'B 'c 'd}
     #{'A 'B 'c 'D}
     #{'A 'b 'C 'D}
     #{'a 'b 'c 'D}
     #{'a 'B 'C 'D}
     #{'A 'B 'C 'd}}))

(assert (= (veitch #{#{'a 'b 'c 'd}
                     #{'a 'B 'c 'd}
                     #{'A 'B 'c 'd}
                     #{'a 'b 'c 'D}
                     #{'a 'B 'c 'D}
                     #{'A 'B 'c 'D}})
   #{#{'a 'c}
     #{'B 'c}}))

(assert (= (veitch #{#{'a 'B 'c 'd}
                     #{'A 'B 'c 'd}
                     #{'a 'b 'c 'D}
                     #{'a 'b 'C 'D}
                     #{'A 'b 'c 'D}
                     #{'A 'b 'C 'D}
                     #{'a 'B 'C 'd}
                     #{'A 'B 'C 'd}})
   #{#{'B 'd}
     #{'b 'D}}))

(assert (= (veitch #{#{'a 'b 'c 'd}
                     #{'A 'b 'c 'd}
                     #{'a 'B 'c 'D}
                     #{'A 'B 'c 'D}
                     #{'a 'B 'C 'D}
                     #{'A 'B 'C 'D}
                     #{'a 'b 'C 'd}
                     #{'A 'b 'C 'd}})
   #{#{'B 'D}
     #{'b 'd}}))
