const { takeRight, range } = require('lodash/fp')

const animals = [
  null,
  ['fly', ''],
  ['spider', '\nIt wriggled and jiggled and tickled inside her.'],
  ['bird', '\nHow absurd to swallow a bird!'],
  ['cat', '\nImagine that, to swallow a cat!'],
  ['dog', '\nWhat a hog, to swallow a dog!'],
  ['goat', '\nJust opened her throat and swallowed a goat!'],
  ['cow', `\nI don't know how she swallowed a cow!`],
  ['horse', `\nShe's dead, of course!`]
]

const reasons =
`She swallowed the cow to catch the goat.
She swallowed the goat to catch the dog.
She swallowed the dog to catch the cat.
She swallowed the cat to catch the bird.
She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.`.split('\n')


class FoodChain {
  verse (n) {
    const [animal, excl] = animals[n]
    const theReasons = n === 8 ? '' : takeRight(n, reasons).join('\n') + '\n'
    return `I know an old lady who swallowed a ${animal}.${excl}\n${theReasons}`
  }
  verses (n, m) {
    return range(n, m + 1).map(this.verse).join('\n') + '\n'
  }
}

module.exports = FoodChain
