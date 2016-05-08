#!/usr/bin/env lein-exec

; Given two sequences x and y, calculate the Levenshtein distance of x
; and y, i. e. the minimum number of edits needed to transform x into y.
; The allowed edits are:

; - insert a single item
; - delete a single item
; - replace a single item with another item

; WARNING: Some of the test cases may timeout if you write an
; inefficient solution!

(defn lev-dist [s t]
  (let [distance
        (memoize (fn [f s t]
                   (if (empty? s) (count t)
                     (if (empty? t) (count s)
                       (min (inc (f f s (butlast t)))
                            (inc (f f t (butlast s)))
                            (+ (if (= (last s) (last t)) 0 1)
                               (f f (butlast s) (butlast t))))))))]
    (distance distance s t)))


(assert (= (lev-dist "kitten" "sitting") 3))
(assert (= (lev-dist "closure" "clojure") (lev-dist "clojure" "closure") 1))
(assert (= (lev-dist "xyx" "xyyyx") 2))
(assert (= (lev-dist "" "123456") 6))
(assert (= (lev-dist "Clojure" "Clojure") (lev-dist "" "") (lev-dist [] []) 0))
(assert (= (lev-dist [1 2 3 4] [0 2 3 4 5]) 2))
(assert (= (lev-dist '(:a :b :c :d) '(:a :d)) 2))
(assert (= (lev-dist "ttttattttctg" "tcaaccctaccat") 10))
(assert (= (lev-dist "gaattctaatctc" "caaacaaaaaattt") 9))
