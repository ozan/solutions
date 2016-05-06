const { eq, reject, spread, zip } = require('lodash/fp')


class Hamming {
  compute (xs, ys) {
    if (xs.length !== ys.length) throw 'DNA strands must be of equal length.'

    const pairs = zip(xs.split(''), ys.split(''))
    return reject(spread(eq), pairs).length
  }
}


module.exports = Hamming
