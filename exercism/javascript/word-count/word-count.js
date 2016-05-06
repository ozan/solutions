const { mapValues, groupBy, identity } = require('lodash/fp')

class Words {
  count (words) {
    const groups = groupBy(identity, words.split(' '))
    return mapValues('length', groups)
  }
}

module.exports = Words
