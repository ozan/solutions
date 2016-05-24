const { reverse, identity } = require('lodash/fp')

const actions = ['wink', 'double blink', 'close your eyes', 'jump']

class SecretHandshake {
  constructor (n) {
    if (typeof n !== 'number') throw Error('Handshake must be a number')
    this.n = n
  }
  commands () {
    const coms = actions.filter((_, i) => (1 << i & this.n) > 0)
    return ((1 << 4 & this.n) > 0 ? reverse : identity)(coms)
  }
}

module.exports = SecretHandshake
