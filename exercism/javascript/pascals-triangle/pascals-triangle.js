const fp = require('lodash/fp')

const pascal = (n) => {
  if (n === 1) return [[1]]
  const upto = pascal(n - 1)
  const prior = upto[upto.length - 1]
  const [xs, ys] = [[0].concat(prior), prior.concat([0])]
  return upto.concat([fp.zip(xs, ys).map(([x, y]) => x + y)])
}

class Triangle {
  constructor (n) {
    this.rows = pascal(n)
    this.lastRow = this.rows[this.rows.length - 1]
  }
}

module.exports = Triangle
