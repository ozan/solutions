const { flow, eq } = require('lodash/fp')


const signature = (word) => {
  const chars = word.toLowerCase().split()
  chars.sort()
  return chars.join('')
}


class Anagram {
  constructor (subject) {
    this.target = signature(subject)
  }
  matches (xs) {
    const match = flow(signature, eq(this.target))
    return xs.filter(match)
  }
}

module.exports = Anagram
