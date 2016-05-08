#!/usr/bin/env lein-exec

; Roman numerals are easy to recognize, but not everyone knows all the
; rules necessary to work with them. Write a function to parse a Roman-
; numeral string and return the number it represents.

; You can assume that the input will be well-formed, in upper-case, and
; follow the subtractive principle. You don't need to handle any numbers
; greater than MMMCMXCIX (3999), the largest number representable with
; ordinary letters.

(defn read-roman [numerals]
  (let [value-of {\M 1000 \D 500 \C 100 \L 50 \X 10 \V 5 \I 1}]
    (loop [[a b & more] numerals
           total 0]
      (if (nil? b) (+ total (value-of a))
          (let [op (if (> (value-of b) (value-of a)) - +)]
            (recur (cons b more) (op total (value-of a))))))))


(assert (= 14 (read-roman "XIV")))
(assert (= 827 (read-roman "DCCCXXVII")))
(assert (= 3999 (read-roman "MMMCMXCIX")))
(assert (= 48 (read-roman "XLVIII")))
