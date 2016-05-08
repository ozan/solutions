#lang racket/base

(require "bob.rkt")

(module+ test
  (require rackunit rackunit/text-ui)

  (define suite
    (test-suite
     "bob tests"

     (test-equal? "responds to something"
                  (response-for "To-may-to, tom-aaaah-to.")
                  "Whatever.")

     (test-equal? "responds to shouts"
                  (response-for "WATCH OUT!")
                  "Whoa, chill out!")

     (test-equal? "responds to questions"
                  (response-for "Does this cryogenic chamber make me look fat?")
                  "Sure.")

     (test-equal? "responds to forceful talking"
                  (response-for "Let's go make out behind the gym!")
                  "Whatever.")

     (test-equal? "responds to acronyms"
                  (response-for "It's OK if you don't want to go to the DMV.")
                  "Whatever.")

     (test-equal? "responds to forceful questions"
                  (response-for "WHAT THE HELL WERE YOU THINKING?")
                  "Whoa, chill out!")

     (test-equal? "responds to shouting with special characters"
                  (response-for "ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!")
                  "Whoa, chill out!")

     (test-equal? "responds to shouting numbers"
                  (response-for "1, 2 ,3, GO!")
                  "Whoa, chill out!")

     (test-equal? "responds to shouting wit no exclamation mark"
                  (response-for "I HATE YOU")
                  "Whoa, chill out!")

     (test-equal? "responds to statement containing question mark"
                  (response-for "Ending with ? means a question.")
                  "Whatever.")

     (test-equal? "responds to silence"
                  (response-for "")
                  "Fine. Be that way!")

     (test-equal? "responds to prolonged-silence"
                  (response-for "     ")
                  "Fine. Be that way!")

     (test-equal? "responds to only-numbers"
                  (response-for "1, 2, 3")
                  "Whatever.")

     (test-equal? "responds to number-question"
                  (response-for "4?")
                  "Sure.")))

  (run-tests suite))
