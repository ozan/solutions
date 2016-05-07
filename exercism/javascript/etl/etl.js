const { forEach } = require('lodash/fp')

class ETL {
  transform (given) {
    const result = {}
    const addScores = (letters, score) =>
      letters.forEach(l => result[l.toLowerCase()] = parseInt(score))
    forEach(addScores, given)
    return result
  }
}

module.exports = ETL
