#!/usr/bin/env node

/*
DP approach: O(width * height) time, O(width) space.

Note: combinatorial approach is much faster and just O(1) space, but
boring. See Python solution for example.
*/

const assert = require('assert')


const last = (xs) => xs[xs.length - 1]

const ones = (n) => Array(n).fill(1)

const addTopAndLeft = (xs, y) => xs.concat(last(xs) + y)

// reducer function which given prior row of DP cache as memo,
// returns subsquent row
const nextRow = (prior, _) => prior.reduce(addTopAndLeft, [0]).slice(1)

const uniquePaths = (width, height) =>
  last(ones(height).reduce(nextRow, ones(width + 1)))

assert.equal(uniquePaths(3, 4), 35)
