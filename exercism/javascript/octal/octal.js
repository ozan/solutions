const fp = require('lodash/fp')

const mapWithKey = fp.map.convert({cap: false})

const octalDigit = (d, i) => d << (i * 3)

class Octal {
  constructor (octalChars) {
    const vals = fp.map(fp.parseInt(8), octalChars)
    this.vals = fp.some(fp.isNaN, vals) ? [] : vals
  }
  toDecimal () {
    return fp.sum(mapWithKey(octalDigit, fp.reverse(this.vals)))
  }
}

module.exports = Octal
