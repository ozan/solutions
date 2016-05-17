module Atbash (encode) where

import Data.Char (toLower, isAlphaNum, isAscii)
import Data.List.Split (chunksOf)
import Data.Map (Map, fromList, (!))

cipher :: Map Char Char
cipher = fromList $ zip (['a'..'z'] ++ ['0'..'9']) (['z','y'..'a'] ++ ['0'..'9'])

encode :: String -> String
encode = unwords . chunksOf 5 . map convert . filter valid
  where valid c = isAscii c && isAlphaNum c
        convert = (cipher !) . toLower
