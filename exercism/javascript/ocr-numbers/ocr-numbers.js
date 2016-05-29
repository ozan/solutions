const {
  flow, map, spread, chunk, split, join, fromPairs, range,
  get: _get, zip: _zip
} = require('lodash/fp')

const get = _get.convert({ fixed: false })
const zip = _zip.convert({ fixed: false })
const transpose = spread(zip)
const lines = split('\n')
const joinLines = join('\n')
const explode = flow(lines, map(split('')))
const unExplode = flow(map(join('')), join(''))
const mapping = flow(Array, transpose, fromPairs)

const splitDigits = flow(
  explode,
  transpose,
  chunk(3),
  map(flow(transpose, unExplode))
)

const nums = mapping(splitDigits(
  ' _     _  _     _  _  _  _  _ \n' +
  '| |  | _| _||_||_ |_   ||_||_|\n' +
  '|_|  ||_  _|  | _||_|  ||_| _|\n' +
  '                              '
), range(0, 10))

const rows = flow(lines, chunk(4), map(joinLines))
const toChar = (sig) => get(sig, nums, '?')
const convertRow = flow(splitDigits, map(toChar), join(''))
const convert = flow(rows, map(convertRow), join(','))

module.exports = { convert }
