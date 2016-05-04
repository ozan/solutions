# Ocr Numbers

Write a program that, given a 3 x 4 grid of pipes, underscores, and spaces, can determine which number is represented, or whether it is garbled.

## Step 1

A simple binary font has been constructed using only pipes and
underscores.

The number is four rows high, three columns wide:

     _   #
    | |  # zero.
    |_|  #
         # the fourth row is always blank

         #
      |  # one.
      |  #
         # (blank fourth row)

Write a program that, given a 3 x 4 grid of pipes, underscores, and
spaces, can determine whether the the grid represents a zero, a one, or
garble.

Anything else is considered garble, and can be represented with a '?'

## Step 2

A simple numeric font has been constructed using only pipes and
underscores.

The number consists of four rows high, three columns wide:

      _  _     _  _  _  _  _  _  #
    | _| _||_||_ |_   ||_||_|| | # decimal numbers.
    ||_  _|  | _||_|  ||_| _||_| #
                                 # fourth line is always blank

There may be several numbers in the input text, one per line.

### Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `exercism/python/<exerciseName>` directory.

For example, if you're submitting `bob.py` for the Bob exercise, the submit command would be something like `exercism submit <path_to_exercism_dir>/python/bob/bob.py`.


For more detailed information about running tests, code style and linting,
please see the [help page](http://exercism.io/languages/python).

## Source

Inspired by the Bank OCR kata [http://codingdojo.org/cgi-bin/wiki.pl?KataBankOCR](http://codingdojo.org/cgi-bin/wiki.pl?KataBankOCR)
