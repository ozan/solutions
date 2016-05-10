module DNA (toRNA) where

import Data.Maybe

al = [('G', 'C'), ('C', 'G'), ('T', 'A'), ('A', 'U')]

toRNA :: String -> String
toRNA dna =
  catMaybes [lookup x al | x <- dna]
