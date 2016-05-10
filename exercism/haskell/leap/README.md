# Leap

Write a program that will take a year and report if it is a leap year.

The tricky thing here is that a leap year in the Gregorian calendar occurs:

```plain
on every year that is evenly divisible by 4
  except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400
```

For example, 1997 is not a leap year, but 1996 is.  1900 is not a leap
year, but 2000 is.

If your language provides a method in the standard library that does
this look-up, pretend it doesn't exist and implement it yourself.

## Notes

Though our exercise adopts some very simple rules, there is more to
learn!

For a delightful, four minute explanation of the whole leap year
phenomenon, go watch [this youtube video][video].

[video]: http://www.youtube.com/watch?v=xX96xng7sAE

Check out [Exercism
Help](http://exercism.io/languages/haskell) for
instructions to get started writing Haskell.

## Running Tests

Use `runhaskell` (included in the Haskell Platform) to compile and run your
Haskell code.

    $ runhaskell -Wall bob_test.hs

## Source

JavaRanch Cattle Drive, exercise 3 [http://www.javaranch.com/leap.jsp](http://www.javaranch.com/leap.jsp)
