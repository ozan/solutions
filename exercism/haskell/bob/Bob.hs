module Bob (responseFor) where

import Data.Char

isYelling :: String -> Bool
isYelling q =
  (q == map toUpper q) && (q /= map toLower q)

isQuestion :: String -> Bool
isQuestion q =
  last q == '?'

isSilence :: String -> Bool
isSilence = all isSpace

responseFor :: String -> String
responseFor q
  | isSilence q = "Fine. Be that way!"
  | isYelling q = "Whoa, chill out!"
  | isQuestion q = "Sure."
  | otherwise = "Whatever."
