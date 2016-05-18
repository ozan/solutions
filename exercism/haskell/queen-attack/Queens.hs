module Queens (boardString, canAttack) where

import Data.List (intercalate, intersperse)


boardString :: Maybe (Int, Int) -> Maybe (Int, Int) -> String
boardString w b = intercalate "\n" rows ++ "\n"
  where rows = map (intersperse ' ') elems
        elems = [[piece (r, c) | c <- [0..7]] | r <- [0..7]]
        piece p
          | Just p == w = 'W'
          | Just p == b = 'B'
          | otherwise = '_'


canAttack :: (Int, Int) -> (Int, Int) -> Bool
canAttack (ar, ac) (br, bc)
  | ar == br = True  -- horizontal
  | ac == bc = True  -- same col -> vertical attack
  | abs (ar - br) == abs (ac - bc) = True  -- diagonal attack
  | otherwise = False
