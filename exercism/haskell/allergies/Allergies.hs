module Allergies (Allergen(..), isAllergicTo, allergies) where

import Data.Bits (shift, (.&.))

data Allergen = Eggs
              | Peanuts
              | Shellfish
              | Strawberries
              | Tomatoes
              | Chocolate
              | Pollen
              | Cats
              deriving (Enum, Show, Eq)

allergies :: Int -> [Allergen]
allergies n = filter (`isAllergicTo` n) (enumFrom Eggs)

isAllergicTo :: Allergen -> Int -> Bool
isAllergicTo a = (> 0) . (.&. shift 1 (fromEnum a))
