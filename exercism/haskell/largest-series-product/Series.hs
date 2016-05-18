module Series (largestProduct) where

import Data.Char (digitToInt)
import Data.List (transpose)

largestProduct :: Int -> String -> Maybe Int
largestProduct n chars
  | n > length chars = Nothing
  | n == 0 = Just 1
  | otherwise = Just
              $ maximum
              $ map product
              $ take (length chars - n + 1)
              $ transpose
              $ take n
              $ iterate (drop 1)
              $ map digitToInt chars
