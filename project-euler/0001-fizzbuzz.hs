#!/usr/bin/env runghc

main = print $ sum [x | x <- [1..999], x `mod` 3 == 0 || x `mod` 5 == 0]
