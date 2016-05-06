const { takeRight } = require('lodash/fp')


class PhoneNumber {
  constructor (str) {
    const digits = str.replace(/[^\d]/g, '')
    if (digits.length === 10 || digits.length === 11 && digits[0] === '1') {
      this.digits = takeRight(10, digits).join('')
    } else {
      this.digits = '0000000000'
    }
  }
  number () {
    return this.digits
  }
  areaCode () {
    return this.digits.slice(0, 3)
  }
  toString () {
    const part = (a, b) => this.digits.slice(a, b)
    return `(${this.areaCode()}) ${part(4, 7)}-${part(8, 11)}`
  }
}

module.exports = PhoneNumber
