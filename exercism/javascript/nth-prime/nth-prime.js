const fp = require('lodash/fp')

function* primes () {
  const known = new Set()
  let candidate = 2
  outer: while (true) {
    for (p of known) {
      if (candidate % p == 0) {
        candidate +=1
        continue outer
      }
    }
    yield candidate
    known.add(candidate)
    candidate += 1
  }
}

const nth = (n) => {
  if (n === 0) throw new Error('Prime is not possible')
  let i = 0
  for (let p of primes()) {
    i++
    if (i === n) return p
  }
}

module.exports = { nth }
