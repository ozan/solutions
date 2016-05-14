module Meetup (Weekday(..), Schedule(..), meetupDay) where

import qualified Data.Map as M
import Data.Time.Calendar
import Data.Time.Calendar.WeekDate

data Weekday = Monday | Tuesday | Wednesday | Thursday | Friday
             | Saturday | Sunday deriving (Enum)

data Schedule = First | Second | Third | Fourth | Teenth | Last deriving (Eq, Ord)


scheduleRange :: Int -> M.Map Schedule [Int]
scheduleRange lastDay = M.fromList [
  (First, [1..7]),
  (Second, [8..14]),
  (Third, [15..21]),
  (Fourth, [22..28]),
  (Teenth, [13..19]),
  (Last, [lastDay-6..lastDay])]


third :: (a, b, c) -> c
third (_, _, a) = a


meetupDay :: Schedule -> Weekday -> Integer -> Int -> Day
meetupDay schedule weekday year month =
  case filter matching dateRange of
    [] -> error "No matches"
    [a] -> a
    _ -> error "More than one match"
  where dayRange = scheduleRange (gregorianMonthLength year month) M.! schedule
        dateRange = map (fromGregorian year month) dayRange
        matching d = third (toWeekDate d) == succ (fromEnum weekday)
