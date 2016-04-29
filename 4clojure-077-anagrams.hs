#!/usr/bin/env runghc

import Data.List (sort)
import Data.Map.Strict (insertWith, elems, empty)

addWord memo word = insertWith (++) (sort word) [word] memo
anagrams words = elems $ foldl addWord empty words

main = print $ anagrams ["veer", "lake", "item", "kale", "mite", "ever"]
