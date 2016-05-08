#!/usr/bin/env lein-exec

; Happy numbers are positive integers that follow a particular formula:
; take each individual digit, square it, and then sum the squares to get
; a new number. Repeat with the new number and eventually, you might get
; to a number whose squared sum is 1. This is a happy number. An unhappy
; number (or sad number) is one that loops endlessly. Write a function
; that determines if a number is happy or not.

(defn happy?
  ([n] (happy? n []))
  ([n seen]
   (let [calc (reduce + (map (comp #(* % %) #(Integer/parseInt %) str) (str n)))]
     (if (= 1 calc)
       true
       (if (contains? seen calc)
         false
         (happy? calc (into [] (cons n seen))))))))


(assert (= (happy? 7) true))
(assert (= (happy? 986543210) true))
(assert (= (happy? 2) false))
(assert (= (happy? 3) false))
