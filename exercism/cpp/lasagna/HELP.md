# Help

## Running the tests

Running the tests involves running `cmake -G` and then using the build command appropriate for your platform.
Detailed instructions on how to do this can be found on the [Running the Tests][cpp-tests-instructions] page for C++ on exercism.org.

## Passing the Tests

When you start a new exercise locally, the files are configured so that only the first test is performed.
Get that first test compiling, linking and passing by following the [three rules of test-driven development][three-laws-of-tdd].
Create just enough structure by declaring namespaces, functions, classes, etc., to satisfy any compiler errors and get the test to fail.
Then write just enough code to get the test to pass.
Once you've done that, uncomment the next test by moving the line `if defined(EXERCISM_RUN_ALL_TESTS)` past the next test.

See the example below from the Bob exercise (file `bob_test.cpp`, line 15):

```diff
-#if defined(EXERCISM_RUN_ALL_TESTS)
TEST_CASE("shouting")
{
    REQUIRE("Whoa, chill out!" == bob::hey("WATCH OUT!"));
}
+#if defined(EXERCISM_RUN_ALL_TESTS)
```

Moving this line past the next test may result in compile errors as new constructs may be invoked that you haven't yet declared or defined.
Again, fix the compile errors minimally to get a failing test, then change the code minimally to pass the test, refactor your implementation for readability and expressiveness and then go on to the next test.

Try to use standard C++17 facilities in preference to writing your own low-level algorithms or facilities by hand.

[cpp-tests-instructions]: https://exercism.org/docs/tracks/cpp/tests
[three-laws-of-tdd]: http://butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd

## Submitting your solution

You can submit your solution using the `exercism submit lasagna.cpp` command.
This command will upload your solution to the Exercism website and print the solution page's URL.

It's possible to submit an incomplete solution which allows you to:

- See how others have completed the exercise
- Request help from a mentor

## Need to get help?

If you'd like help solving the exercise, check the following pages:

- The [C++ track's documentation](https://exercism.org/docs/tracks/cpp)
- The [C++ track's programming category on the forum](https://forum.exercism.org/c/programming/cpp)
- [Exercism's programming category on the forum](https://forum.exercism.org/c/programming/5)
- The [Frequently Asked Questions](https://exercism.org/docs/using/faqs)

Should those resources not suffice, you could submit your (incomplete) solution to request mentoring.

To get help if you're having trouble, you can use one of the following resources:

- [`c++-faq` tag on StackOverflow](https://stackoverflow.com/tags/c%2b%2b-faq/info)
- [C++ FAQ from isocpp.com](https://isocpp.org/faq)
- [CppReference](http://en.cppreference.com/) is a wiki reference to the C++ language and standard library
- [C traps and pitfalls](http://www.slideshare.net/LegalizeAdulthood/c-traps-and-pitfalls-for-c-programmers) is useful if you are new to C++, but have programmed in C