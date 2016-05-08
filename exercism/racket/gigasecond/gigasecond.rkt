#lang racket

(provide add-gigasecond)

(require racket/date)

(define (add-gigasecond dt)
  (seconds->date (+ 1e9 (date->seconds dt))))
