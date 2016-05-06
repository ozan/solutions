const _ = { get } = require('lodash/fp')

const mapping = {G: 'C', C: 'G', T: 'A', A: 'U'}

class DnaTranscriber {
  toRna (chars) {
    return chars.split('').map(get(_, mapping)).join('')
  }
}

module.exports = DnaTranscriber
