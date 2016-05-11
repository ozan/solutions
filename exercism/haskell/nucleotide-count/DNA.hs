module DNA (count, nucleotideCounts) where

import Data.Maybe (fromMaybe)
import qualified Data.Map as Map
import qualified Data.Set as Set

initial :: Map.Map Char Int
initial = Map.fromList [('A', 0), ('T', 0), ('C', 0), ('G', 0)]

isValid :: Char -> Bool
isValid ch =
  Set.member ch $ Set.fromList "ATCG"

invalidNucleotide :: Char -> String
invalidNucleotide ch =
  "invalid nucleotide '" ++ [ch] ++ "'"

incNucleotide :: Map.Map Char Int -> Char -> Map.Map Char Int
incNucleotide counts ch
  | isValid ch = Map.adjust (1 +) ch counts
  | otherwise = error $ invalidNucleotide ch

nucleotideCounts :: String -> Map.Map Char Int
nucleotideCounts =
  foldl incNucleotide initial

count :: Char -> String -> Int
count ch strand =
  fromMaybe (error $ invalidNucleotide ch) (Map.lookup ch $ nucleotideCounts strand)
