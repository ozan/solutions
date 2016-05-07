const BigInt = require('./big-integer')

const two = BigInt(2)

class Grains {
  square (n) {
    return two.pow(n - 1).toString()
  }
  total () {
    return two.pow(64).minus(1).toString()
  }
}

module.exports = Grains
