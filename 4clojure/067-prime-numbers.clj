#!/usr/bin/env lein-exec

; Write a function which returns the first x number of prime numbers.

(defn first-primes [n]
 (loop [primes [2 3]
  candidate 5]
  (if (= n (count primes))
   primes
   (if (every? #(> (mod candidate %) 0) primes)
    (recur (conj primes candidate) (+ 2 candidate))
    (recur primes (+ 2 candidate))))))


(assert (= (first-primes 2) [2 3]))
(assert (= (first-primes 5) [2 3 5 7 11]))
(assert (= (last (first-primes 100)) 541))
