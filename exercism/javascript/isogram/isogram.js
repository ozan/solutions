
class Isogram {
  constructor (word) {
    this.word = word.replace(new RegExp('[- ]', 'g'), '')
  }
  isIsogram () {
    return this.word.length == new Set(this.word.toLowerCase()).size
  }
}

module.exports = Isogram
