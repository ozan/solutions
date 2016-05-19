const fp = require('lodash/fp')

const join = fp.join('')
const zip = fp.zip.convert({fixed: false})

class Crypto {
  constructor (rawMessage) {
    this.message = rawMessage.toLowerCase().replace(/[^a-z0-9]/g, '')
  }

  normalizePlaintext () {
    return this.message
  }

  size () {
    return Math.ceil(Math.sqrt(this.message.length))
  }

  plaintextSegments () {
    return fp.map(join, this._chunks())
  }

  ciphertext () {
    const transpose = zip.apply(null, this._chunks())
    return fp.flow(
      fp.flatten,
      fp.compact,
      join
    )(transpose)
  }

  _chunks () {
    return fp.chunk(this.size(), this.normalizePlaintext())
  }
}

module.exports = Crypto
