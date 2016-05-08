#!/usr/bin/env lein-exec

; Write a function which behaves like reduce, but returns each
; intermediate value of the reduction. Your function must accept either
; two or three arguments, and the return sequence must be lazy.

(defn seq-reductions
  ([f xs] (seq-reductions f (first xs) (rest xs)))
  ([f a xs]
   (lazy-seq
    (let [[b & others] xs
          comb (f a b)]
      (if (empty? others)
        (cons a [comb])
        (cons a (seq-reductions f comb others)))))))


(assert (= (take 5 (seq-reductions + (range))) [0 1 3 6 10]))
(assert (= (seq-reductions conj [1] [2 3 4]) [[1] [1 2] [1 2 3] [1 2 3 4]]))
(assert (= (last (seq-reductions * 2 [3 4 5])) (reduce * 2 [3 4 5]) 120))
