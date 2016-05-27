const isPalindrome = (n) =>
  String(n) === String(n).split('').reverse().join('')


class Palindromes {
  constructor ({maxFactor, minFactor=1}) {
    this.maxFactor = maxFactor
    this.minFactor = minFactor
  }
  generate () {
    const factors = {}
    for (let a = this.minFactor; a <= this.maxFactor; a++) {
      for (let b = a; b <= this.maxFactor; b++) {
        if (isPalindrome(a * b)) {
          factors[a*b] = (factors[a*b] || []).concat([[a, b]])
        }
      }
    }
    this.results = Object.keys(factors)
      .map(k => [Number(k), factors[k]])
      .sort((a, b) => a[0] - b[0])
  }
  largest () {
    // assumes generate has been called, per tests
    const [value, factors] = this.results[this.results.length - 1]
    return { value, factors }
  }
  smallest () {
    // assumes generate has been called, per tests
    const [value, factors] = this.results[0]
    return { value, factors }
  }
}

module.exports = Palindromes
