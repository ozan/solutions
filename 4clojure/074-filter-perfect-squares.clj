#!/usr/bin/env lein-exec

; Given a string of comma separated integers, write a function which
; returns a new comma separated string that only contains the numbers
; which are perfect squares.

(defn perfect-squares [xs]
  (clojure.string/join "," (map str (filter
   #(= 0.0 (mod (Math/sqrt (Integer/parseInt %)) 1))
   (clojure.string/split xs #"\,")))))

(assert (= (perfect-squares "4,5,6,7,8,9") "4,9"))
(assert (= (perfect-squares "15,16,25,36,37") "16,25,36"))
