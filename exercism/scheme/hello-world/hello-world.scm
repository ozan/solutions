(define-module (hello-world)
  #:export (hello))

(use-modules (ice-9 format))

(define (hello name)
  (format #f "Hello, ~a!" name))

(define (hello)
  (hello "World"))

(display (hello))
