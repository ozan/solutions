# Grep

Search a file for lines matching a regular expression pattern. Return the line number and contents of each matching line.

Given a string `filename` and regular expression `pattern`, collect and
return the line numbers and contents of all lines in the file denoted by
`filename` that match `pattern`.

In other words, solutions should open the file described by `filename`
and read each of its lines while keeping track of line numbers (starting at 1).
If a line matches `pattern`, create a pair containing the line's
number and the line itself.
After reading the entire file, return a list of all such pairs sorted
from lowest line number to highest.

The name "grep" comes from the [Unix program](http://pubs.opengroup.org/onlinepubs/9699919799/utilities/grep.html) with the same name.
(In Unix, "grep" was a mnemonic for a useful command to another program [sed](http://www.gnu.org/software/sed/manual/sed.html), whose name means "stream editor".)

The Unix `grep` can be run from the command line and accepts a variety of flags.
Try reproducing some of these in your implementation. For example:
- Accept a pattern and list of files on the command-line, print results
  for each file to the console.
- Implement the flags:
  - `-l` Print only the names of files that contain at least one matching line.
  - `-v` Invert the program -- collect all lines that fail to match the pattern.
  - `-x` Only match entire lines, instead of lines that contain a match.
- Support multiple flags at once.
  For example, running `grep -l -x "hello" file1.txt file2.txt` should
  print the names of files that do not contain the string "hello"

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

Conversation with Nate Foster. [http://www.cs.cornell.edu/Courses/cs3110/2014sp/hw/0/ps0.pdf](http://www.cs.cornell.edu/Courses/cs3110/2014sp/hw/0/ps0.pdf)
