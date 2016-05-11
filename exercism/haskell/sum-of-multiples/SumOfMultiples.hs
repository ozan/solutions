module SumOfMultiples (sumOfMultiples) where

anyDivide :: [Int] -> Int -> Bool
anyDivide divisors n =
  any (\d -> n `mod` d == 0) divisors

sumOfMultiples :: [Int] -> Int -> Int
sumOfMultiples divisors limit =
  sum $ filter (anyDivide divisors) [1..limit - 1]
