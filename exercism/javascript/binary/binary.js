const { map, add } = require('lodash/fp')


class Binary {
  constructor (bin) {
    this.digits = bin.match(/[^10]/) ? [] : map(parseInt, bin.split(''))
  }
  toDecimal () {
    return this.digits.reverse().map((dig, i) => dig << i).reduce(add, 0)
  }
}

module.exports = Binary
