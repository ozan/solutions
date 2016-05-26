# Wordy

Write a program that takes a word problem and returns the answer as an integer.

## Step 1

E.g.

> What is 5 plus 13?

The program should handle large numbers and negative numbers.

Remember, that these are verbal word problems, not treated as you
normally would treat a written problem.  This means that you calculate
as you move forward each step.  In other words, you should ignore order
of operations.  3 + 2 * 3 = 15, not 9.

Use the tests to drive your solution by deleting the `skip` in one test
at a time.

## Step 2

E.g.

> What is 5 plus 13?

> What is 7 minus 5?

> What is 6 multiplied by 4?

> What is 25 divided by 5?

## Step 3

E.g.

> What is 5 plus 13 plus 6?

> What is 7 minus 5 minus 1?

> What is 9 minus 3 plus 5?

> What is 3 plus 5 minus 8?

## Step 4

E.g.

> What is 5 plus 13?

> What is 7 minus 5?

> What is 6 times 4?

> What is 25 divided by 5?

> What is 78 plus 5 minus 3?

> What is 18 times 3 plus 16?

> What is 4 times 3 divided by 6?

> What is 4 plus 3 times 2?

## Extensions

Implement questions of the type:

> What is 2 raised to the 5th power?

Remember to write failing tests for this code.

## Setup

Go through the setup instructions for JavaScript to
install the necessary dependencies:

http://exercism.io/languages/javascript

## Making the Test Suite Pass

Execute the tests with:

    jasmine-node .

In many test suites all but the first test have been skipped.

Once you get a test passing, you can unskip the next one by
changing `xit` to `it`.

## Source

Inspired by one of the generated questions in the Extreme Startup game. [https://github.com/rchatley/extreme_startup](https://github.com/rchatley/extreme_startup)
