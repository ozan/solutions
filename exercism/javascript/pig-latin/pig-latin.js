const fp = require('lodash/fp')

const translate = (phrase) =>
  phrase.split(' ').map(translateWord).join(' ')

const translateWord = (word) =>
  splitOnSound(word).join('') + 'ay'

const consonant = Symbol('c')
const vowel = Symbol('v')
const as = (y, xs) => xs.map(x => [y, x])
const rules = fp.flatten([
  as(consonant, ['ch', 'qu', 'squ', 'thr', 'th', 'sch']),
  as(vowel, ['yt', 'xr']),
  as(consonant, 'bcdfghjklmnpqrstvwxyz'.split('')),
  as(vowel, 'aeiou'.split(''))
])

const splitOnSound = (word) =>
  fp.flow(
    fp.filter(ruleFits(word)),
    fp.map(partOrder(word)),
    fp.compact,
    fp.head
  )(rules)

const ruleFits = fp.curry((word, [_, stem]) =>
  stem === word.slice(0, stem.length))

const partOrder = fp.curry((word, [type, stem]) =>
  (type === vowel ? fp.identity : fp.reverse)(
    [stem, word.slice(stem.length)]))

module.exports = { translate }
