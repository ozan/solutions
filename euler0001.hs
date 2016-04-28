#!/usr/bin/env runghc

sumMultiples x y upto =
  sum [0,x..upto] + sum [0,y..upto] - sum [0,x*y..upto]

main = print (sumMultiples 3 5 999)
