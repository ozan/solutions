#!/usr/bin/env lein-exec


; Write an oscillating iterate: a function that takes an initial value
; and a variable number of functions. It should return a lazy sequence
; of the functions applied to the value in order, restarting from the
; first function after it hits the end.

(defn oscilrate [x f & funcs]
  (lazy-seq
   (let [y (f x)
         next-funcs (concat funcs [f])]
     (cons x (apply oscilrate y next-funcs)))))


(assert (= (take 3 (oscilrate 3.14 int double)) [3.14 3 3.0]))
(assert (= (take 5 (oscilrate 3 #(- % 3) #(+ 5 %))) [3 0 5 2 7]))
(assert (= (take 12 (oscilrate 0 inc dec inc dec inc)) [0 1 0 1 0 1 2 1 2 1 2 3]))
