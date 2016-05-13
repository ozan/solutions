module School (School, add, empty, sorted, grade) where

import Data.List (sort)
import qualified Data.Map as Map

type Grade = Int
type Student = String
type School = Map.Map Grade [Student]

empty :: School
empty = Map.empty

add :: Grade -> Student -> School -> School
add k v = Map.insertWith (++) k [v]

sorted :: School -> [(Grade, [Student])]
sorted = Map.toList . Map.map sort

grade :: Grade -> School -> [Student]
grade = Map.findWithDefault []
