module Strain (keep, discard) where

keep :: (a -> Bool) -> [a] -> [a]
keep f = foldr (\x xs -> if f x then x : xs else xs) []

discard :: (a -> Bool) -> [a] -> [a]
discard = keep . (not .)
