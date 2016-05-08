#!/usr/bin/env lein-exec

; In a family of languages like Lisp, having balanced parentheses is a
; defining feature of the language. Luckily, Lisp has almost no syntax,
; except for these "delimiters" -- and that hardly qualifies as
; "syntax", at least in any useful computer programming sense.

; It is not a difficult exercise to find all the combinations of well-
; formed parentheses if we only have N pairs to work with. For instance,
; if we only have 2 pairs, we only have two possible combinations:
; "()()" and "(())". Any other combination of length 4 is ill-formed.
; Can you see why?

; Generate all possible combinations of well-formed parentheses of
; length 2n (n pairs of parentheses). For this problem, we only consider
; '(' and ')', but the answer is similar if you work with only {} or
; only [].

; There is an interesting pattern in the numbers!

(defn gen-parens
  ([n] (if (= 0 n) #{""} (set (gen-parens n 0))))
  ([n open]
   (if (= 0 n)
     (vector (apply str (repeat open ")")))
     (if (= 0 open)
       (map #(str "(" %) (gen-parens (dec n) 1))
       (concat
         (map #(str ")" %) (gen-parens n (dec open)))
         (map #(str "(" %) (gen-parens (dec n) (inc open))))))))


(assert (= [#{""} #{"()"} #{"()()" "(())"}] (map (fn [n] (gen-parens n)) [0 1 2])))
(assert (= #{"((()))" "()()()" "()(())" "(())()" "(()())"} (gen-parens 3)))
(assert (= 16796 (count (gen-parens 10))))
(assert (= (nth (sort (filter #(.contains ^String % "(()()()())") (gen-parens 9))) 6) "(((()()()())(())))"))
(assert (= (nth (sort (gen-parens 12)) 5000) "(((((()()()()()))))(()))"))
