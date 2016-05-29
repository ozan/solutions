const { range, sum, some } = require('lodash/fp')

const SumOfMultiples = (factors) => ({
  to: (limit) => {
    const multiples = range(1, limit).filter(m => some(d => m % d == 0, factors))
    return sum(multiples)
  }
})

module.exports = SumOfMultiples
