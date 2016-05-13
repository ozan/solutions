module Phone (areaCode, number, prettyPrint) where

import Data.Char (isDigit)
import Text.Printf (printf)

invalid :: String
invalid = "0000000000"

number :: String -> String
number given
  | length digits == 10 = digits
  | length digits == 11 && head digits == '1' = tail digits
  | otherwise = invalid
  where digits = filter isDigit given


areaCode :: String -> String
areaCode = slice 0 3 . number


prettyPrint :: String -> String
prettyPrint given = printf "(%s) %s-%s" area major minor
  where num = number given
        [area, major, minor] = map ($ num) [areaCode, slice 3 3, slice 6 4]


slice :: Int -> Int -> String -> String
slice a n = take n . drop a
