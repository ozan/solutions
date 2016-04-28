#!/usr/bin/env runghc

fib = 1 : 1 : [a + b | (a, b) <- zip fib (tail fib)]

main = print $ sum $ filter (even) $ takeWhile (<4000000) fib
