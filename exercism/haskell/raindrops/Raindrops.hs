module Raindrops (convert) where

cases :: [(Int, String)]
cases = [
  (3, "Pling"),
  (5, "Plang"),
  (7, "Plong")]

convert :: Int -> String
convert n = if null matches then show n else concat matches
  where matches = map snd $ filter ((== 0) . rem n . fst) cases
