module Raindrops (convert) where

cases :: [(Int, String)]
cases = [
  (3, "Pling"),
  (5, "Plang"),
  (7, "Plong")]

convert :: Int -> String
convert n = if null matches then show n else concat matches
  where matches = [plxng | (p, plxng) <- cases, n `rem` p == 0]
