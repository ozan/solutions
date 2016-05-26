const fp = require('lodash/fp')

const operation = {
  plus: fp.add,
  minus: fp.subtract,
  divided: fp.divide,
  multiplied: fp.multiply
}

const toToken = (str) =>
  Number(str) || operation[str]

const tokenize = (phrase) =>
  fp.compact(phrase.split(' ').map(toToken))

const foldIn = (a, [f, b]) => f(a, b)

const evaluate = (tokens) =>
  fp.chunk(2, fp.tail(tokens)).reduce(foldIn, tokens[0])

class WordProblem {
  constructor (question) {
    this.tokens = tokenize(question.replace('?', ''))
  }
  answer () {
    if (this.tokens.length < 3) throw new ArgumentError()
    return evaluate(this.tokens)
  }
}

class ArgumentError extends Error {}

module.exports = { WordProblem, ArgumentError }
