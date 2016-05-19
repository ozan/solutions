const fp = require('lodash/fp')

class Trinary {
  constructor (repr) {
    const digits = repr.split('').reverse().map(fp.parseInt(10))
    const valid = !fp.some(fp.isNaN, digits)
    this.digits = valid ? digits : []
  }

  toDecimal () {
    const places = this.digits.map((d, i) => d * Math.pow(3, i))
    return fp.sum(places)
  }
}

module.exports = Trinary
