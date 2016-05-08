#!/usr/bin/env lein-exec

; A palindromic number is a number that is the same when written
; forwards or backwards (e.g., 3, 99, 14341).

; Write a function which takes an integer n, as its only argument, and
; returns an increasing lazy sequence of all palindromic numbers that
; are not less than n.

; The most simple solution will exceed the time limit!

(defn generate-palindromes [start]
  (let [next-palindrome (fn[n]
                          (let [int-to-digits (fn [n] (map #(- (int %) (int \0)) (str n)))
                                digits-to-int #(read-string (apply str %))
                                is-even? #(= 0 (mod (count %) 2))
                                get-left #(take (Math/ceil (/ (count %) 2)) %)
                                mirror-even #(concat % (reverse %))
                                mirror-odd #(concat % (rest (reverse %)))
                                digits (int-to-digits n)
                                mirror (if (is-even? digits) mirror-even mirror-odd)
                                other-mirror (if (is-even? digits) mirror-odd mirror-even)
                                left-digits (get-left digits)
                                mirrored-digits (mirror left-digits)
                                candidate (digits-to-int mirrored-digits)]
                            (if (> candidate n) candidate
                              (let [higher-num (inc (digits-to-int left-digits))
                                    higher-digits (int-to-digits higher-num)
                                    higher-candidate (digits-to-int (mirror higher-digits))]
                                (if (= (count higher-digits) (count left-digits))
                                  higher-candidate
                                  (let [trunc (if (is-even? digits) higher-digits (butlast higher-digits))]
                                    (digits-to-int (other-mirror trunc))))))))

        first-palindrome (if (= 0 start) 0 (next-palindrome (dec start)))
        ]
    (iterate next-palindrome first-palindrome)))


(assert (= (take 26 (generate-palindromes 0))
   [0 1 2 3 4 5 6 7 8 9
    11 22 33 44 55 66 77 88 99
    101 111 121 131 141 151 161]))
(assert (= (take 16 (generate-palindromes 162))
   [171 181 191 202
    212 222 232 242
    252 262 272 282
    292 303 313 323]))
(assert (= (take 6 (generate-palindromes 1234550000))
   [1234554321 1234664321 1234774321
    1234884321 1234994321 1235005321]))
(assert (= (first (generate-palindromes (* 111111111 111111111)))
   (* 111111111 111111111)))
(assert (= (set (take 199 (generate-palindromes 0)))
   (set (map #(first (generate-palindromes %)) (range 0 10000)))))
(assert (= true
   (apply < (take 6666 (generate-palindromes 9999999)))))
(assert (= (nth (generate-palindromes 0) 10101)
   9102019))
