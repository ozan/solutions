#!/usr/bin/env lein-exec

; Write a function which generates the transitive closure of a binary
; relation. The relation will be represented as a set of 2 item vectors.

(defn tc [s]
  (letfn [(get-related [s [a b]] (filter (fn [[c d]] (= b c)) s))
          (get-deep-related [s [a b]]
                            (let [related (get-related s [a b])]
                              (if (empty? related) []
                                (concat related (mapcat (partial get-deep-related s) related)))))]
    (clojure.set/union
      s
      (into #{} (apply concat (for [[a b] s]
                                (let [related (get-deep-related s [a b])]
                                  (map (fn [[c d]] (vector a d)) related))))))))


(assert (let [divides #{[8 4] [9 3] [4 2] [27 9]}]
  (= (tc divides) #{[4 2] [8 4] [8 2] [9 3] [27 9] [27 3]})))
(assert (let [more-legs
      #{["cat" "man"] ["man" "snake"] ["spider" "cat"]}]
  (= (tc more-legs)
     #{["cat" "man"] ["cat" "snake"] ["man" "snake"]
       ["spider" "cat"] ["spider" "man"] ["spider" "snake"]})))
(assert (let [progeny
      #{["father" "son"] ["uncle" "cousin"] ["son" "grandson"]}]
  (= (tc progeny)
     #{["father" "son"] ["father" "grandson"]
       ["uncle" "cousin"] ["son" "grandson"]})))

