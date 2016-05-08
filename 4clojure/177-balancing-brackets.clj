#!/usr/bin/env lein-exec

; When parsing a snippet of code it's often a good idea to do a sanity
; check to see if all the brackets match up. Write a function that takes
; in a string and returns truthy if all square [ ] round ( ) and curly {
; } brackets are properly paired and legally nested, or returns falsey
; otherwise.

(defn balanced? [string]
  (let [pairs {\( \) \[ \] \{ \}}]
    (loop [[ch & more] string
           stack []]
      (if (nil? ch) (empty? stack)  ; at the end, non-empty stack indicates too many left symbols
          (if (pairs ch) (recur more (cons ch stack))  ; put left symbols on the stack
              (if (some #{ch} (vals pairs))  ; for right hand symbols, ensure matches top of stack
                (and (= ch (pairs (first stack))) (recur more (rest stack)))
                (recur more stack)))))))


(assert (balanced? "This string has no brackets."))
(assert (balanced? "class Test {
      public static void main(String[] args) {
        System.out.println(\"Hello world.\");
      }
    }"))
(assert (not (balanced? "(start, end]"))
(assert (not (balanced? "())"))))
(assert (not (balanced? "[ { ] } ")))
(assert (balanced? "([]([(()){()}(()(()))(([[]]({}()))())]((((()()))))))"))
(assert (not (balanced? "([]([(()){()}(()(()))(([[]]({}([)))())]((((()()))))))")))
(assert (not (balanced? "[")))
