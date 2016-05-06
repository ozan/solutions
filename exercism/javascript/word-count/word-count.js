const { mapValues, groupBy, identity } = require('lodash/fp')

const parse = (str) =>
  str.trim().toLowerCase().replace('  ', ' ').split(/[ \t\n]/g)

class Words {
  count (words) {
    const groups = groupBy(identity, parse(words))
    return mapValues('length', groups)
  }
}

module.exports = Words
