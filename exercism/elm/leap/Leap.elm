module Leap (..) where

isLeapYear : Int -> Bool
isLeapYear year =
  let
    multipleOf = \n -> year % n == 0
  in
    (multipleOf 400)
      || (multipleOf 4) && (not (multipleOf 100))
