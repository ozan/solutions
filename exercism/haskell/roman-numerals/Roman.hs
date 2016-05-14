module Roman (numerals) where


parts :: [(Int, String)]
parts = [
  (1000, "M"),
  (900, "CM"),
  (500, "D"),
  (400, "CD"),
  (100, "C"),
  (90, "XC"),
  (50, "L"),
  (49, "IL"),
  (40, "XL"),
  (10, "X"),
  (9, "IX"),
  (5, "V"),
  (4, "IV"),
  (1, "I")]


numerals :: Int -> String
numerals 0 = ""
numerals n = roman ++ numerals (n - part)
  where (part, roman) = head $ filter ((<= n) . fst) parts
