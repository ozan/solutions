module Anagram (anagramsFor) where

import Data.Char (toLower)
import Data.List (sort)

lower :: String -> String
lower = map toLower

key :: String -> String
key = sort . lower

anagramsFor :: String -> [String] -> [String]
anagramsFor word =
  filter (\ch -> key ch == key word && lower ch /= lower word)
