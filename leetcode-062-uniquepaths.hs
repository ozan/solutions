#!/usr/bin/env runghc

ones n = take n $ repeat 1
next prior = 0 : [p + n | (p, n) <- zip prior (next prior)]
nextRow prior _ = tail $ next prior
uniquePaths width height = last $ foldl nextRow [1..height] (ones width)

main = print $ uniquePaths 3 4 -- 35
