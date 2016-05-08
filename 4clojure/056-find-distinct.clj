#!/usr/bin/env lein-exec

; Write a function which removes the duplicates from a sequence. Order
; of the items must be maintained.

(defn find-distinct [xs]
 ((fn inner [done left]
   (if (empty? left)
    done
    (let [n (first left)]
     (if (some #{n} done)
      (inner done (rest left))
      (inner (concat done [n]) (rest left))))))
 () xs))

(assert (= (find-distinct [1 2 1 3 1 2 4]) [1 2 3 4]))
(assert (= (find-distinct [:a :a :b :b :c :c]) [:a :b :c]))
(assert (= (find-distinct '([2 4] [1 2] [1 3] [1 3])) '([2 4] [1 2] [1 3])))
(assert (= (find-distinct (range 50)) (range 50)))

