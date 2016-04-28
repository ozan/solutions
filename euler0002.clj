#!/usr/bin/env lein-exec

(defn fib []
  (map first (iterate (fn [[a b]] [b (+ a b)])
                      [0 1])))

(defn fib-sum [limit]
  (apply + (take-while #(< %1 limit) (filter even? (fib)))))


(println (fib-sum 4e6))
