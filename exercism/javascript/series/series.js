const fp = require('lodash/fp')

const zip = fp.zip.convert({fixed: false})

class Series {
  constructor (n) {
    this.digits = n.split('').map(fp.parseInt(10))
  }
  slices (n) {
    if (n > this.digits.length) throw new Error('Slice size is too big.')
    if (n === 1) return this.digits.map(d => [d])
    const steps = fp.map(fp.drop(fp, this.digits), fp.range(0, n))
    return zip.apply(null, steps).slice(0, this.digits.length + 1 - n)
  }
}

module.exports = Series
