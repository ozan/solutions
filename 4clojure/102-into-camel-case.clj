#!/usr/bin/env lein-exec

; When working with java, you often need to create an object with
; fieldsLikeThis, but you'd rather work with a hashmap that has :keys-
; like-this until it's time to convert. Write a function which takes
; lower-case hyphen-separated strings and converts them to camel-case
; strings.

(defn into-camel [word]
 (clojure.string/join ""
  (let [sp (clojure.string/split word #"\-")]
   (cons (first sp) (map clojure.string/capitalize (rest sp))))))


(assert (= (into-camel "something") "something"))
(assert (= (into-camel "multi-word-key") "multiWordKey"))
(assert (= (into-camel "leaveMeAlone") "leaveMeAlone"))
