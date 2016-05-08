#!/usr/bin/env lein-exec

; A balanced prime is a prime number which is also the mean of the
; primes directly before and after it in the sequence of valid primes.
; Create a function which takes an integer n, and returns true iff it is
; a balanced prime.

(defn is-balanced? [p]
  (if (< p 3) false
    (let [mean-in-middle (fn [[a b c]] (= b (/ (+ a c) 2)))
          penultimate #(last (butlast %))]
      (loop [primes [2 3]
             candidate 5]
        (if (= p (penultimate primes))
          (mean-in-middle (subvec primes (- (count primes) 3)))
          (if (< p (penultimate primes))
            false
            (if (every? #(> (mod candidate %) 0) primes)
              (recur (conj primes candidate) (+ 2 candidate))
              (recur primes (+ 2 candidate)))))))))


(assert (= false (is-balanced? 4)))
(assert (= true (is-balanced? 563)))
(assert (= 1103 (nth (filter is-balanced? (range)) 15)))
