const fp = require('lodash/fp')

const zip = fp.zip.convert({fixed: false})

class Matrix {
  constructor (str) {
    const parse = fp.flow(fp.split(' '), fp.map(fp.parseInt(10)))
    this.rows = str.split('\n').map(parse)
    this.columns = zip.apply(null, this.rows)
  }
}

module.exports = Matrix
