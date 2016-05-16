module PrimeFactors (primeFactors) where

primeFactors :: Int -> [Int]
primeFactors 1 = []
primeFactors n = p:primeFactors(n `div` p)
  where p = head $ filter ((== 0) . rem n) (2:[3,5..n])
