
class Raindrops {
  convert (n) {
    const c = (p, word) => n % p == 0 ? word : ''
    return `${c(3, 'Pling')}${c(5, 'Plang')}${c(7, 'Plong')}` || String(n)
  }
}

module.exports = Raindrops
