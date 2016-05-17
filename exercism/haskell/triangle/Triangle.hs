module Triangle (TriangleType(..), triangleType) where

import qualified Data.Set as Set
import Data.List (sort)

data TriangleType = Illogical
                  | Equilateral
                  | Isosceles
                  | Scalene
                  deriving (Show, Eq, Enum)

triangleType :: Int -> Int -> Int -> TriangleType
triangleType a b c
  | a' + b' <= c' = Illogical
  | any (<= 0) [a, b, c] = Illogical
  | otherwise = toEnum equalSides::TriangleType
  where [a', b', c'] = sort [a, b, c]
        equalSides = Set.size $ Set.fromList [a, b, c]
