const fp = require('lodash/fp')

const rng = fp.range(0, 8)

class Queens {
  constructor ({ white = [0, 3], black = [7, 3] } = {}) {
    this.white = white
    this.black = black
  }
  toString () {
    return rng.map(i => rng.map(j => this.charAt(i, j)).join(' ')).join('\n') + '\n'
  }
  charAt (i, j) {
    return deq([i, j], this.white) && 'W' ||
           deq([i, j], this.black) && 'B' || '_'
  }
  canAttack () {
    const [wx, wy] = this.white
    const [bx, by] = this.black
    return wx === bx || wy === by || Math.abs(wx - bx) === Math.abs(wy - by)
  }
}

module.exports = Queens
