const _ = require('lodash/fp')

const mapping = {G: 'C', C: 'G', T: 'A', A: 'U'}

class DnaTranscriber {
  toRna (chars) {
    return chars.split().map(_.get(_, mapping)).join()
  }
}

module.exports = DnaTranscriber
