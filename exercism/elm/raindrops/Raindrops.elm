module Raindrops (..) where

import String

cases : List (Int, String)
cases = [
  (3, "Pling"),
  (5, "Plang"),
  (7, "Plong")]


raindrops : Int -> String
raindrops n =
  let
    matches = List.filter (\c -> n % (fst c) == 0) cases
  in
    if (List.isEmpty matches) then
      toString n
    else
      String.join "" (List.map snd matches)
