#!/usr/bin/env lein-exec

; A word chain consists of a set of words ordered so that each word
; differs by only one letter from the words directly before and after
; it. The one letter difference can be either an insertion, a deletion,
; or a substitution. Here is an example word chain:

; cat -> cot -> coat -> oat -> hat -> hot -> hog -> dog

; Write a function which takes a sequence of words, and returns true if
; they can be arranged into one continous word chain, and false if they
; cannot.

(defn chainable? [words]
  (let [connected? (fn connected? [[a & rest-a] [b & rest-b]]
                     (if (= a b) (connected? rest-a rest-b)
                       (or (= rest-a (cons b rest-b)) ; addition
                           (= rest-a rest-b) ; substitution
                           (= (cons a rest-a) rest-b)))) ; subtraction
        connections-of (fn [word] (filter #(and (not= word %) (connected? word %)) words))
        adjacencies (into {} (map #(vector % (connections-of %)) words))
        chain? (fn chain? [visited word]
                 (if (= (count words) (inc (count visited))) true
                   (some (partial chain? (conj visited word))
                         (clojure.set/difference (into #{} (get adjacencies word)) visited))))]
    (boolean (some (partial chain? #{}) words))))


(assert (= true (chainable? #{"hat" "coat" "dog" "cat" "oat" "cot" "hot" "hog"})))
(assert (= false (chainable? #{"cot" "hot" "bat" "fat"})))
(assert (= false (chainable? #{"to" "top" "stop" "tops" "toss"})))
(assert (= true (chainable? #{"spout" "do" "pot" "pout" "spot" "dot"})))
(assert (= true (chainable? #{"share" "hares" "shares" "hare" "are"})))
(assert (= false (chainable? #{"share" "hares" "hare" "are"})))
