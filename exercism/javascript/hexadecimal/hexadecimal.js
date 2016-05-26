const { some, eq, sum } = require('lodash/fp')

const toDec = (ch) => '0123456789abcdef'.indexOf(ch)

class Hexadecimal {
  constructor (chars) {
    const digits = chars.split('').map(toDec)
    this.digits = some(eq(-1), digits) ? [] : digits
  }
  toDecimal () {
    return sum(this.digits.reverse().map((d, i) => d << (4*i)))
  }
}

module.exports = Hexadecimal
