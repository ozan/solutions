module Hexadecimal (hexToInt) where

import Data.Bits (shift)
import qualified Data.Map as M
import Data.Maybe (isNothing)

digits :: M.Map Char Int
digits = M.fromList $ zip "0123456789abcdef" [0..]

hexToInt :: String -> Int
hexToInt hex
  | any (isNothing . (`M.lookup` digits)) hex = 0
  | otherwise = sum $ map (uncurry shift) ranks
  where ranks = zip (map (digits M.!) $ reverse hex) [0,4..]
