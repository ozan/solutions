const fp = require('lodash/fp')

const sieve = (upto) => {
  const primes = [null, null].concat(fp.range(2, upto + 1))
  let p = 2
  nextprime:
  while (true) {
    for (let i = 2*p; i < primes.length; i += p) {
      primes[i] = null
    }
    for (i=p+1; i < primes.length; i++) {
      if (primes[i]) {
        p = primes[i]
        continue nextprime
      }
    }
    return fp.compact(primes)
  }
  return primes
}

class Sieve {
  constructor (n) {
    this.primes = sieve(n)
  }
}

module.exports = Sieve
