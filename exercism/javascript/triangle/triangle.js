const _ = { any, lte, sortBy, identity } = require('lodash/fp')

class Triangle {
  constructor (a, b, c) {
    this.sides = sortBy(identity, [a, b, c])
  }
  kind () {
    const [a, b, c] = this.sides
    const s = new Set(this.sides)

    if (any(lte(_, 0), this.sides)) throw Error('Invalid sides')
    if (a + b <= c) throw Error('Triangle inequality violated')

    return ['wat', 'equilateral', 'isosceles', 'scalene'][s.size]
  }
}

module.exports = Triangle
