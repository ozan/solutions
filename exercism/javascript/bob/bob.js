const { constant, cond, last } = require('lodash/fp')

const yell = (q) => q === q.toUpperCase() && q.match(/[a-zA-Z]/)
const question = (q) => last(q) === '?'
const empty = (q) => q.trim() === ''
const otherwise = constant(true)

const cases = [
  [yell, constant('Whoa, chill out!')],
  [question, constant('Sure.')],
  [empty, constant('Fine. Be that way!')],
  [otherwise, constant('Whatever.')]
]

class Bob {
  hey (q) {
    return cond(cases)(q)
  }
}

module.exports = Bob
