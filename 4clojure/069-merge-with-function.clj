#!/usr/bin/env lein-exec

; Write a function which takes a function f and a variable number of
; maps. Your function should return a map that consists of the rest of
; the maps conj-ed onto the first. If a key occurs in more than one map,
; the mapping(s) from the latter (left-to-right) should be combined with
; the mapping in the result by calling (f val-in-result val-in-latter)

(defn merg-with [f m & maps]
 (if (empty? maps) m
  (let [n (first maps)]
   (apply merg-with
    (concat [f (into {}
                (for [k (concat (keys m) (keys n))]
                 (let [vm (get m k)
                       vn (get n k)]
                  (if (nil? vm) [k vn]
                   (if (nil? vn) [k vm]
                    [k (f vm vn)])))))]
    (rest maps))))))


(assert (= (merg-with * {:a 2, :b 3, :c 4} {:a 2} {:b 2} {:c 5})
   {:a 4, :b 6, :c 20}))

(assert (= (merg-with - {1 10, 2 20} {1 3, 2 10, 3 15})
   {1 7, 2 10, 3 15}))

(assert (= (merg-with concat {:a [3], :b [6]} {:a [4 5], :c [8 9]} {:b [7]})
   {:a [3 4 5], :b [6 7], :c [8 9]}))
