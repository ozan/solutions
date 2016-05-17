module CryptoSquare (normalizePlaintext,
                     squareSize,
                     plaintextSegments,
                     ciphertext,
                     normalizeCiphertext) where

import Data.Char (toLower, isAlphaNum)
import Data.List (transpose)
import Data.List.Split (chunksOf)

normalizePlaintext :: String -> String
normalizePlaintext = map toLower . filter isAlphaNum

squareSize :: String -> Int
squareSize x = ceiling $ sqrt len
  where len = fromIntegral (length x) :: Float

plaintextSegments :: String -> [String]
plaintextSegments text = chunksOf (squareSize cleaned) cleaned
  where cleaned = normalizePlaintext text

ciphertext :: String -> String
ciphertext = concat . transpose . plaintextSegments

normalizeCiphertext :: String -> String
normalizeCiphertext = unwords . transpose . plaintextSegments
