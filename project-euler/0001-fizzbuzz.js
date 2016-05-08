#!/usr/bin/env node

const range = (n) => Array(n).fill().map((_, i) => i)

const sum = (xs) => xs.reduce((x1, x2) => x1 + x2)

console.log(sum(range(1000).filter(n => n % 3 === 0 || n % 5 === 0)))
