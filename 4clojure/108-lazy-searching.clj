#!/usr/bin/env lein-exec

; Given any number of sequences, each sorted from smallest to largest,
; find the smallest single number which appears in all of the sequences.
; The sequences may be infinite, so be careful to search lazily.

(defn lazy-search [& seqs]
  (let [smallest (first (first seqs))
        dropped (map (fn [xs] (drop-while #(< % smallest) xs)) seqs)
        firsts (map first dropped)]
    (if (apply = firsts)
      smallest
      (apply lazy-search (cons (rest (first dropped)) (rest dropped))))))


(assert (= 3 (lazy-search [3 4 5])))
(assert (= 4 (lazy-search [1 2 3 4 5 6 7] [0.5 3/2 4 19])))
(assert (= 7 (lazy-search (range) (range 0 100 7/6) [2 3 5 7 11 13])))
(assert (= 64 (lazy-search (map #(* % % %) (range)) ;; perfect cubes
          (filter #(zero? (bit-and % (dec %))) (range)) ;; powers of 2
          (iterate inc 20)))) ;; at least as large as 20
