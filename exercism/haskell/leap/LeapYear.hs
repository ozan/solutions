module LeapYear (isLeapYear) where

isLeapYear :: Int -> Bool
isLeapYear year =
  let mult n = year `rem` n == 0
  in mult 400 || mult 4 && not (mult 100)
