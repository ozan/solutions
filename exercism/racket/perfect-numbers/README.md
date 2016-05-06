# Perfect Numbers

The Greek mathematician Nicomachus devised a classification scheme for natural numbers.

The Greek mathematican Nicomachus devised a classification scheme for
natural numbers, identifying each as belonging uniquely to the
categories of _abundant_, _perfect_, or _deficient_.  A perfect number
equals the sum of its positive divisors — the pairs of numbers whose
product yields the target number, excluding the number itself.

- Perfect: Sum of factors = number
- Abundant: Sum of factors > number
- Deficient: Sum of factors < number

The Aliquot sum is defined as the sum of the factors of a number not
including the number itself.

## Examples

- 6 is a perfect number because its divisors are 1, 2, 3 and 6 = 1 + 2 +
  3.
- 28 is perfect number because 28 = 1 + 2 + 4 + 7 + 14.
- Prime numbers 7, 13, etc are Deficient by the Nicomachus
  classificaton.

* * * *

For installation and learning resources, refer to the
[exercism Racket page](http://exercism.io/languages/racket).

You can run the provided tests through DrRacket, or via the command line.

To run the test through DrRacket, simply open the test file and click the 'Run' button in the upper right.

To run the test from the command line, simply run the test from the exercise directory. For example, if the test suite is called `hello-world-test.rkt`, you can run the following command:

```
raco test hello-world-test.rkt
```

which will display the following:

```
raco test: (submod "hello-world-test.rkt" test)
2 success(es) 0 failure(s) 0 error(s) 2 test(s) run
0
2 tests passed
```

## Source

Taken from Chapter 2 of Functional Thinking by Neal Ford. [http://shop.oreilly.com/product/0636920029687.do](http://shop.oreilly.com/product/0636920029687.do)
