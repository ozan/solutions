#!/usr/bin/env lein-exec

; Create a function of no arguments which returns a string that is an
; exact copy of the function itself.

(assert (= (str '(fn [x] (str x x)) '(fn [x] (str x x)))
           ((fn [x] (str x x)) '(fn [x] (str x x)))))
