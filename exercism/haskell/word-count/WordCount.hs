module WordCount (wordCount) where

import Control.Arrow
import Data.Map as Map (Map, fromList)
import Data.Char (toLower, isAlphaNum)
import Data.List (group, sort)
import Data.List.Split (wordsBy)


wordCount :: String -> Map String Int
wordCount phrase = fromList counts
  where tokenize = wordsBy (not . isAlphaNum) . map toLower
        groups = group . sort . tokenize
        counts = map (head &&& length) (groups phrase)
