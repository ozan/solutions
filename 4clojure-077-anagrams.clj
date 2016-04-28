#!/usr/bin/env lein-exec

(defn anagrams [words]
   (->> words
        (group-by sort)
        (vals)
        (filter #(> (count %) 1))
        (map set)
        (set)))

(println (anagrams ["veer" "lake" "item" "kale" "mite" "ever"]))
