# Pacman Rules

Welcome to Pacman Rules on Exercism's C++ Track.
If you need help running the tests or submitting your code, check out `HELP.md`.
If you get stuck on the exercise, check out `HINTS.md`, but try and solve it without using those first :)

## Introduction

Booleans in C++ are represented by the `bool` type.
A `bool` is either `true` or `false`.

## Logical Operators

C++ supports three boolean operators: `!` (NOT), `&&` (AND), and `||` (OR).
You can also use the alternative versions `not`, `and`, and `or`.

```cpp
true || false // => true
true && false // => false
!true // => false
not false // => true
```

## Precedence

The three boolean operators each have different _operator precedence_.
As a consequence, they are evaluated in this order: `!` first, `&&` second, and finally `||`.
If you want to force a different ordering, you can enclose a boolean expression in parentheses (ie. `()`), as the parentheses have even higher operator precedence.

```cpp
!true && false   // => false
!(true and false) // => true
```

~~~~exercism/advanced
## Conversion

If you use `true` or `false` in a place where a number is expected, they will be converted to  `1` and `0` respectively.
If you use a number in a Boolean operation, everything except `0` is treated as `true` - even negative values.

```cpp
!true && 0.0   // => false
true + true + false // => 2
```
~~~~

## Instructions

In this exercise, you need to translate some rules from the classic game Pac-Man into C++ functions.

You have four rules to translate, all related to the game states.

> Don't worry about how the arguments are derived, just focus on combining the arguments to return the intended result.

## 1. Define if Pac-Man eats a ghost

Define the `can_eat_ghost` function that takes two arguments (_if Pac-Man has a power pellet active_ and _if Pac-Man is touching a ghost_) and returns a boolean value if Pac-Man is able to eat the ghost. The function should return true only if Pac-Man has a power pellet active and is touching a ghost.

```cpp
can_eat_ghost(false, true);
// => false
```

## 2. Define if Pac-Man scores

Define the `scored` function that takes two arguments (_if Pac-Man is touching a power pellet_ and _if Pac-Man is touching a dot_) and returns a boolean value if Pac-Man scored. The function should return true if Pac-Man is touching a power pellet or a dot.

```cpp
scored(true, true);
// => true
```

## 3. Define if Pac-Man loses

Define the `lost` function that takes two arguments (_if Pac-Man has a power pellet active_ and _if Pac-Man is touching a ghost_) and returns a boolean value if Pac-Man loses. The function should return true if Pac-Man is touching a ghost and does not have a power pellet active.

```cpp
lost(false, true);
// => true
```

## 4. Define if Pac-Man wins

Define the `won` function that takes three arguments (_if Pac-Man has eaten all of the dots_, _if Pac-Man has a power pellet active_, and _if Pac-Man is touching a ghost_) and returns a boolean value if Pac-Man wins. The function should return true if Pac-Man has eaten all of the dots and has not lost based on the arguments defined in part 3.

```cpp
won(false, true, false);
// => false
```

## Source

### Created by

- @vaeng