module Bob where

import String

isYelling : String -> Bool
isYelling q =
  (q == String.toUpper q) && (q /= String.toLower q)

isQuestion : String -> Bool
isQuestion q =
  String.endsWith "?" q

isSilence : String -> Bool
isSilence q =
  (String.trim q) == ""

cases = [
  (isYelling, "Whoa, chill out!"),
  (isQuestion, "Sure."),
  (isSilence, "Fine. Be that way!")]

hey : String -> String
hey q =
  case (List.head (List.filter (\c -> (fst c) q) cases)) of
    Just c -> snd c
    Nothing -> "Whatever."
