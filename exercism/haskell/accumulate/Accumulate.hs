module Accumulate (accumulate) where

accumulate :: Foldable t => (a -> a1) -> t a -> [a1]
accumulate f = foldr ((:) . f) []
