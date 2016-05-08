#!/usr/bin/env lein-exec

; This is the inverse of Problem 92, but much easier. Given an integer
; smaller than 4000, return the corresponding roman numeral in
; uppercase, adhering to the subtractive principle.

(defn to-roman [n]
  (let [thousands ["" "M" "MM" "MMM" "MMMM"]
        hundreds ["" "C" "CC" "CCC" "CD" "D" "DC" "DCC" "DCCC" "CM"]
        tens ["" "X" "XX" "XXX" "XL" "L" "LX" "LXX" "LXXX" "XC"]
        units ["" "I" "II" "III" "IV" "V" "VI" "VII" "VIII" "IX"]
        positions [units tens hundreds thousands]
        char-to-digit (zipmap (seq "0123456789") (range 10))
        digits (map char-to-digit (seq (str n)))
        position-digits (map-indexed vector (reverse digits))
        chars (map (fn [[pos val]] ((positions pos) val)) position-digits)]
    (apply str (reverse chars))))


(assert (= "I" (to-roman 1)))
(assert (= "XXX" (to-roman 30)))
(assert (= "IV" (to-roman 4)))
(assert (= "CXL" (to-roman 140)))
(assert (= "DCCCXXVII" (to-roman 827)))
(assert (= "MMMCMXCIX" (to-roman 3999)))
(assert (= "XLVIII" (to-roman 48)))
