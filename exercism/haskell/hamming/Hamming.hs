module Hamming (distance) where

distance :: String -> String -> Int
distance xs ys =
  length [1 | (x, y) <- zip xs ys, x /= y] 
