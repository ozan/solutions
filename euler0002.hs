
fib n
  | n < 2 = 1
  | otherwise = fib (n - 1) + fib (n - 2)

main = print (sum (filter (even) (takeWhile (<4000000) (map fib [1..]))))
