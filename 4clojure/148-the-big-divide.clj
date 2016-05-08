#!/usr/bin/env lein-exec

; Write a function which calculates the sum of all natural numbers under
; n (first argument) which are evenly divisible by at least one of a and
; b (second and third argument). Numbers a and b are guaranteed to be
; coprimes.

; Note: Some test cases have a very large n, so the most obvious
; solution will exceed the time limit.

(defn big-divide [num a b]
   (let [ar-sum (fn [m n] (* m (+ n 1) (/ n 2)))
         how-many (fn [m] (bigint (/ (dec num) m)))]
     (- (+ (ar-sum a (how-many a))
           (ar-sum b (how-many b)))
        (ar-sum (* a b) (how-many (* a b))))))


(assert (= 0 (big-divide 3 17 11)))
(assert (= 23 (big-divide 10 3 5)))
(assert (= 233168 (big-divide 1000 3 5)))
(assert (= "2333333316666668" (str (big-divide 100000000 3 5))))
(assert (= "110389610389889610389610"
  (str (big-divide (* 10000 10000 10000) 7 11))))
(assert (= "1277732511922987429116"
  (str (big-divide (* 10000 10000 10000) 757 809))))
(assert (= "4530161696788274281"
  (str (big-divide (* 10000 10000 1000) 1597 3571))))
