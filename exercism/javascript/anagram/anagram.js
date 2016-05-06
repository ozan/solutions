const { reject, eq, flow } = require('lodash/fp')


const signature = (word) => {
  const chars = word.toLowerCase().split('')
  const foo = chars.sort()
  return chars.join('')
}


class Anagram {
  constructor (subject) {
    this.subject = subject
  }
  matches (xs) {
    const match = x => signature(x) === signature(this.subject)
    const same = x => x.toLowerCase() === this.subject.toLowerCase()
    return reject(same, xs.filter(match))
  }
}

module.exports = Anagram
