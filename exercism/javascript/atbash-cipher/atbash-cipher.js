const _ = { chunk, identity, fromPairs, zip } = require('lodash/fp')

const alpha = 'abcdefghijklmnopqrstuvwxyz'.split('')
const atbash = alpha.slice()
atbash.reverse()
const digits = '01234566789'.split('')
const conv = fromPairs(zip(alpha.concat(digits), atbash.concat(digits)))

const convert = (str) =>
  str.toLowerCase().split('').map(ch => conv[ch] || '').filter(identity)

const format = (str) =>
  chunk(5, str).map(chars => chars.join('')).join(' ')


const encode = (str) =>
  format(convert(str))

module.exports = { encode }
