const fp = require('lodash/fp')

const mapWithIndex = fp.map.convert({cap: false})

const digits = (n) =>
  String(n).split('').map(fp.parseInt(10))

const trans = (d, i) =>
  i % 2 == 0 ? d : (d < 5 ? d * 2 : d * 2 - 9)

class Luhn {
  constructor (n) {
    this.checkDigit = n % 10
    this.addends = fp.reverse(mapWithIndex(trans, fp.reverse(digits(n))))
    this.checksum = fp.sum(this.addends)
    this.valid = this.checksum % 10 == 0
  }
}

Luhn.create = (n) => {
  const candidate = n * 10
  const checksum = new Luhn(candidate).checksum % 10
  return candidate + (10 - checksum) % 10
}

module.exports = Luhn
