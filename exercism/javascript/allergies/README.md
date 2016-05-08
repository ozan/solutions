# Allergies

Write a program that, given a person's allergy score, can tell them whether or not they're allergic to a given item, and their full list of allergies.

An allergy test produces a single numeric score which contains the
information about all the allergies the person has (that they were
tested for).

The list of items (and their value) that were tested are:

* eggs (1)
* peanuts (2)
* shellfish (4)
* strawberries (8)
* tomatoes (16)
* chocolate (32)
* pollen (64)
* cats (128)

So if Tom is allergic to peanuts and chocolate, he gets a score of 34.

Now, given just that score of 34, your program should be able to say:

- Whether Tom is allergic to any one of those allergens listed above.
- All the allergens Tom is allergic to.

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

Jumpstart Lab Warm-up [http://jumpstartlab.com](http://jumpstartlab.com)
