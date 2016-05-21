#lang racket

(provide
  grep-file)

(define (grep-file path pattern)
  (let* ((lines (file->lines path))
         (line-numbers (range 1 (add1 (length lines))))
         (pairs (map cons line-numbers lines))
         (does-match? (lambda (p) (regexp-match pattern (cdr p)))))
    (filter does-match? pairs)))


(module+ main
  (let* ((args (vector->list (current-command-line-arguments)))
         (pattern (regexp (car args)))
         (paths (rest args)))
    (for* ((path paths)
           (result (grep-file path pattern)))
      (printf "~a:~a\n" path (cdr result)))))
