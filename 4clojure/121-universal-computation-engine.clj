#!/usr/bin/env lein-exec

; Given a mathematical formula in prefix notation, return a function
; that calculates the value of the formula. The formula can contain
; nested calculations using the four basic mathematical operators,
; numeric constants, and symbols representing variables. The returned
; function has to accept a single parameter containing the map of
; variable names to their values.

(defn uct [[op-sym & args]]
  (let [operator (get {'/ / '* * '+ + '- -} op-sym)]
    (fn [vars]
      (let [calculate (fn [exp]
                        (if (seq? exp) ((uct exp) vars)
                          (or (vars exp) exp)))]
        (apply operator (map calculate args)))
      )))


(assert (= 2 ((uct '(/ a b))
      '{b 8 a 16})))

(assert (= 8 ((uct '(+ a b 2))
      '{a 2 b 4})))

(assert (= [6 0 -4]
     (map (uct '(* (+ 2 a)
                  (- 10 b)))
            '[{a 1 b 8}
              {b 5 a -2}
              {a 2 b 11}])))

(assert (= 1 ((uct '(/ (+ x 2)
              (* 3 (+ y 1))))
      '{x 4 y 1})))
