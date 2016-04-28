#!/usr/bin/env node

function* fib () {
  let a = 0
  let b = 1
  let temp
  while (true) {
    [a, b] = [b, a + b]
    yield a
  }
}

const f = (upto) => {
  let total = 0
  for (let n of fib()) {
    if (n > upto) break
    if (n % 2 == 0) total += n
  }
  return total
}

console.log(f(4e6))
