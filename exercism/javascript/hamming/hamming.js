const { eq, zip } = require('lodash/fp')


class Hamming {
  compute (xs, ys) {
    return zip(xs, ys).filter(eq.apply).length
  }
}


module.exports = Hamming
