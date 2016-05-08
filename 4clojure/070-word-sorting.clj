#!/usr/bin/env lein-exec

; Write a function that splits a sentence up into a sorted list of
; words. Capitalization should not affect sort order and punctuation
; should be ignored.


(defn sort-words [sentence]
 (sort
  (fn compare-words [word-a word-b]
   (let [lower-first (fn [word] (int (first (clojure.string/lower-case (first word)))))
    a (lower-first word-a)
    b (lower-first word-b)]
    (cond
     (every? nil? [a b]) 0
     (< a b) -1
     (> a b) 1
     :else (compare-words (rest word-a) (rest word-b)))))
  (clojure.string/split sentence #"\W")))


(assert (= (sort-words  "Have a nice day.")
   ["a" "day" "Have" "nice"]))

(assert (= (sort-words  "Clojure is a fun language!")
   ["a" "Clojure" "fun" "is" "language"]))

(assert (= (sort-words  "Fools fall for foolish follies.")
   ["fall" "follies" "foolish" "Fools" "for"]))
