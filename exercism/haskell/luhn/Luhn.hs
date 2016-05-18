module Luhn (checkDigit, addends, checksum, isValid, create) where

import Data.List (unfoldr)
import qualified Data.Map as M

checkDigit :: Integer -> Integer
checkDigit = (`mod` 10)

addends :: Integer -> [Integer]
addends n = reverse $ unfoldr f (n, 0)
  where f (0, _) = Nothing
        f (m, par) = Just (conv par (m `rem` 10), (m `div` 10, (par + 1) `mod` 2))
        conv par = (M.!) (mappings !! par)
        sing = M.fromList $ zip [0..9] [0..9]
        doub = M.fromList $ zip [0..9] [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
        mappings = [sing, doub]

checksum :: Integer -> Integer
checksum = (`mod` 10) . sum . addends

isValid :: Integer -> Bool
isValid n = checksum n `mod` 10 == 0

create :: Integer -> Integer
create n = n * 10 + (- checksum (n * 10)) `mod` 10
