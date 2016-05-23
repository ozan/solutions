const fp = require('lodash/fp')

const ord = (ch) =>
  ch.charCodeAt(0) - 97

const chr = (n) =>
  String.fromCharCode(n + 97)

const charOp = fp.curry((f, x, y) =>
  x && y ? chr(f(ord(x), ord(y)) % 26) : '')

const zipStringsWith = (f, xs, ys) =>
  fp.zipWith(f, xs.split(''), ys.split('')).join('')

const inRange = (n) =>
  n >= 0 && n <= 26


class Cipher {
  constructor (key) {
    if (key === '' || !fp.every(inRange, fp.map(ord, key))) {
      throw new Error('Bad key')
    }
    this.key = key || 'ddddddddddddddddd'
  }
  encode (secret) {
    return zipStringsWith(charOp(fp.add), secret, this.key)
  }
  decode (crypt) {
    return zipStringsWith(charOp(fp.subtract), crypt, this.key)
  }
}

module.exports = Cipher
