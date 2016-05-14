module Binary (toDecimal) where

import Data.Char (isDigit)
import Data.Bits (shift)

val :: Char -> Int
val '1' = 1
val _ = 0

toDecimal :: String -> Int
toDecimal chars
  | all isDigit chars = sum vals
  | otherwise = 0
  where vals = map (uncurry shift) places
        places = zip (reverse $ map val chars) [0..]
