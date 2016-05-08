#!/usr/bin/env lein-exec

; Clojure has many sequence types, which act in subtly different ways.
; The core functions typically convert them into a uniform "sequence"
; type and work with them that way, but it can be important to
; understand the behavioral and performance differences so that you know
; which kind is appropriate for your application.

; Write a function which takes a collection and returns one of :map,
; :set, :list, or :vector - describing the type of collection it was
; given. You won't be allowed to inspect their class or use the built-in
; predicates like list? - the point is to poke at them and understand
; their behavior.

(defn seq-type [seq]
 (let [t (conj (empty seq) [:k :v])]
  (cond
   (:k t) :map
   (get t 0) :vector
   (get t [:k :v]) :set
   :else :list)))

(assert (= :map (seq-type {:a 1, :b 2})))
(assert (= :list (seq-type (range (rand-int 20)))))
(assert (= :vector (seq-type [1 2 3 4 5 6])))
(assert (= :set (seq-type #{10 (rand-int 5)})))
(assert (= [:map :set :vector :list] (map seq-type [{} #{} [] ()])))
