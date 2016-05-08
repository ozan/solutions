#!/usr/bin/env lein-exec

; A function f defined on a domain D induces an equivalence relation on
; D, as follows: a is equivalent to b with respect to f if and only if
; (f a) is equal to (f b). Write a function with arguments f and D that
; computes the equivalence classes of D with respect to f.

(defn equiv [f s]
  (set (map set (vals (group-by f s)))))


(assert (= (equiv #(* % %) #{-2 -1 0 1 2})
   #{#{0} #{1 -1} #{2 -2}}))

(assert (= (equiv #(rem % 3) #{0 1 2 3 4 5 })
   #{#{0 3} #{1 4} #{2 5}}))

(assert (= (equiv identity #{0 1 2 3 4})
   #{#{0} #{1} #{2} #{3} #{4}}))

(assert (= (equiv (constantly true) #{0 1 2 3 4})
   #{#{0 1 2 3 4}}))

