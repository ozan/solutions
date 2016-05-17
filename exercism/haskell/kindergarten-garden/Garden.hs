module Garden (garden, defaultGarden, lookupPlants, Plant(..)) where

import Data.List (sort, transpose)
import Data.List.Split (chunksOf)
import qualified Data.Map as M

type Rows = String  -- e.g. "VVCG\nVVRC"
type Child = String  -- e.g. "Alice"
type Garden = M.Map Child [Plant]
data Plant = Violets | Grass | Clover | Radishes deriving (Show, Eq, Enum)

plants :: M.Map Char Plant
plants = M.fromList $ zip "VGCR" (enumFrom Violets)

defaultChildren :: [Child]
defaultChildren = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
                   "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]

garden :: [Child] -> Rows -> Garden
garden kids rows = M.fromList $ zip (sort kids) allotment
  where allotment = map concat
                  . transpose
                  . map (chunksOf 2 . map (plants M.!))
                  . lines $ rows

defaultGarden :: Rows -> Garden
defaultGarden = garden defaultChildren

lookupPlants :: Child -> Garden -> [Plant]
lookupPlants = flip (M.!)
