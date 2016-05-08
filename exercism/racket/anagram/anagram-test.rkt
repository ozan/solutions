#lang racket/base

(require "anagram.rkt")

(module+ test
  (require rackunit rackunit/text-ui))

(module+ test
  (define allergies '("gallery" "ballerina" "regally" "clergy" "largely" "leading"))

  (define suite
    (test-suite
     "anagram tests"

     (test-equal? "no-matches"
                  (anagrams-for "diaper" '("hello" "world" "zombies" "pants"))
                  '())

     (test-equal? "detect simple anagram"
                  (anagrams-for "ant" '("tan" "stand" "at"))
                  '("tan"))

     (test-equal? "does not confuse different duplicates"
                  (anagrams-for "galea" '("eagle"))
                  '())

     (test-equal? "eliminate anagram subsets"
                  (anagrams-for "good" '("dog" "goody"))
                  '())

     (test-equal? "detect anagram"
                  (anagrams-for "listen"'("enlists" "google" "inlets" "banana"))
                  '("inlets"))

     (test-equal? "multiple-anagrams"
                  (anagrams-for "allergy" allergies)
                  '("gallery" "regally" "largely"))

     (test-equal? "case-insensitive-anagrams"
                  (anagrams-for "Orchestra" '("cashregister" "Carthorse" "radishes"))
                  '("Carthorse"))

     (test-equal? "word is not own anagram"
                  (anagrams-for "banana"'("banana"))
                  '())))

  (run-tests suite))
