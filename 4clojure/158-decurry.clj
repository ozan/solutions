#!/usr/bin/env lein-exec


; Write a function that accepts a curried function of unknown arity n. Return an equivalent function of n arguments.

(defn decurry [f]
  (fn inner [x & args]
    (if (empty? args)
        (f x)
        (apply (decurry (f x)) args))))


(assert (= 10 ((decurry (fn [a]
             (fn [b]
               (fn [c]
                 (fn [d]
                   (+ a b c d))))))
       1 2 3 4)))

(assert (= 24 ((decurry (fn [a]
             (fn [b]
               (fn [c]
                 (fn [d]
                   (* a b c d))))))
       1 2 3 4)))

(assert (= 25 ((decurry (fn [a]
             (fn [b]
               (* a b))))
       5 5)))
