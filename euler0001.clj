#!/usr/bin/env lein-exec

(defn divisible-by [n div]
  (= 0 (mod n div)))

(defn sum-multiples [a b upto]
  (apply +
    (filter #(or (divisible-by %1 a)
                 (divisible-by %1 b))
            (range 0 upto))))

(println (sum-multiples 3 5 1000))
