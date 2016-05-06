const { constant, cond, last } = require('lodash/fp')

const question = (q) => last(q) === '?'
const yell = (q) => q === q.toUpperCase()
const empty = (q) => q === ''
const otherwise = constant(true)

const cases = [
  [question, constant('Sure')],
  [yell, constant('Whoa, chill out!')],
  [empty, constant('Fine. Be that way!')],
  [otherwise, constant('Whatever.')]
]

class Bob {
  hey (q) {
    return cond(cases)(q)
  }
}

module.exports = Bob
