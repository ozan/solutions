
class Pangram {
  constructor (sentence) {
    this.chars = new Set(sentence.toLowerCase().replace(/[^a-z]/g, ''))
  }
  isPangram () {
    return this.chars.size === 26
  }
}

module.exports = Pangram
