const fp = require('lodash/fp')

class Queue {
  constructor (limit) {
    this.limit = limit || Infinity
    this.vals = []
  }
  push (v) {
    this.vals.push(v)
    while (this.vals.length > this.limit) {
      this.vals.shift()
    }
  }
}

function* products (digits, n) {
  const q = new Queue(n)
  for (let d of digits) {
    q.push(d)
    if (q.vals.length === n) {
      yield q.vals.reduce(fp.multiply)
    }
  }
}

class Series {
  constructor (chars) {
    const digits = chars.split('').map(fp.parseInt(10))
    if (fp.some(fp.isNaN, digits)) throw new Error('Invalid input.')
    this.digits = digits
  }
  largestProduct (n) {
    if (n < 0) throw new Error('Invalid input.')
    if (n > this.digits.length) throw new Error('Slice size is too big.')
    if (n === 0) return 1
    const candidates = Array.from(products(this.digits, n))
    return Math.max.apply(null, candidates)
  }
}

module.exports = Series
