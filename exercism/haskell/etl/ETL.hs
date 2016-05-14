module ETL (transform) where

import qualified Data.Char as C
import qualified Data.List as L
import qualified Data.Map as M

type Old = M.Map Int [String]
type New = M.Map String Int

transform :: Old -> New
transform old = M.fromList pairs
  where pairs = L.concatMap valsToKeys (M.assocs old)
        valsToKeys (k, vals) = L.map (allValsFor k) vals
        allValsFor k v = (map C.toLower v, k)
