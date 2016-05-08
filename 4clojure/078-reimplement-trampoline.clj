#!/usr/bin/env lein-exec

; Reimplement the function described in "Intro to Trampoline".

(defn tramp
  ([f]
   (let [ret (f)]
     (if (fn? ret)
       (recur ret)
       ret)))
  ([f & args]
   (tramp #(apply f args))))


(assert (= (letfn [(triple [x] #(sub-two (* 3 x)))
          (sub-two [x] #(stop?(- x 2)))
          (stop? [x] (if (> x 50) x #(triple x)))]
    (tramp triple 2))
  82))

(assert (= (letfn [(my-even? [x] (if (zero? x) true #(my-odd? (dec x))))
          (my-odd? [x] (if (zero? x) false #(my-even? (dec x))))]
    (map (partial tramp my-even?) (range 6)))
  [true false true false true false]))
