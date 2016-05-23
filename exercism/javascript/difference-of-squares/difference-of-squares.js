const fp = require('lodash/fp')

const square = (n) => n * n

class Squares {
  constructor (n) {
    this.n = n
    this.sumOfSquares = fp.sum(fp.range(1, n + 1).map(square))
    this.squareOfSums = square(fp.sum(fp.range(1, n + 1)))
    this.difference = this.squareOfSums - this.sumOfSquares
  }
}

module.exports = Squares
