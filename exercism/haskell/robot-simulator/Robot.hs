module Robot (Bearing(..), Robot, mkRobot,
              coordinates, simulate,
              bearing, turnRight, turnLeft) where

import qualified Data.Map as M

data Bearing = North | East | South | West deriving (Eq, Enum, Show, Ord)
type Coords = (Int, Int)
data Robot = Robot { bearing :: Bearing
                   , coordinates :: Coords
                   } deriving (Eq, Show)

deltas :: M.Map Bearing Coords
deltas = M.fromList $ zip (enumFrom North) [(0, 1), (1, 0), (0, -1), (-1, 0)]

addC :: Coords -> Coords -> Coords
addC (ax, ay) (bx, by) = (ax + bx, ay + by)

turnLeft :: Bearing -> Bearing
turnLeft = turn (-1)

turnRight :: Bearing -> Bearing
turnRight = turn 1

turn :: Int -> Bearing -> Bearing
turn n b = toEnum ((n + fromEnum b) `mod` 4)::Bearing

mkRobot :: Bearing -> Coords -> Robot
mkRobot = Robot

simulate :: Robot -> String -> Robot
simulate = foldl followDirection

followDirection :: Robot -> Char -> Robot
followDirection robot char = case char of
  'L' -> Robot (turnLeft bear) coords
  'R' -> Robot (turnRight bear) coords
  'A' -> Robot bear (coords `addC` (M.!) deltas bear)
  _ -> error "Invalid instruction"
  where bear = bearing robot
        coords = coordinates robot
