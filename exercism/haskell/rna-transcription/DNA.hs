module DNA (toRNA) where

import Data.Maybe (mapMaybe)

dnaToRna :: [(Char, Char)]
dnaToRna = [('G', 'C'), ('C', 'G'), ('T', 'A'), ('A', 'U')]

toRNA :: String -> String
toRNA = mapMaybe (`lookup` dnaToRna)
