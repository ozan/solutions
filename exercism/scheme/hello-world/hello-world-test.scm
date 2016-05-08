;; Load SRFI-64 lightweight testing specification
(use-modules (srfi srfi-64))

;; Suppress log file output. To write logs, comment out the following line:
(module-define! (resolve-module '(srfi srfi-64)) 'test-log-to-file #f)

;; Require module
(add-to-load-path (dirname (current-filename)))
(use-modules (hello-world))

(test-begin "hello-world")

(test-assert "Called with no args returns hello world"
             (equal? (hello)
                     "Hello, World!"))

(test-assert "Called with an arg returns hello arg"
             (equal? (hello "exercism")
                     "Hello, exercism!"))

(test-end "hello-world")
