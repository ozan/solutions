
const factors = (n) => {
  if (n === 1) return []
  if (n % 2 == 0) return [2].concat(factors(n / 2))
  for (let k = 3; k <= n; k+=2) {
    if (n % k == 0) return [k].concat(factors(n / k))
  }
  throw Error('Invalid input')
}

module.exports = { for: factors }
