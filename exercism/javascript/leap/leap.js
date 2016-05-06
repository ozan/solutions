
const div = (n, d) =>
  n % d == 0


class Year {
  constructor (year) {
    this.year = year
  }
  isLeap () {
    return div(this.year, 400) || div(this.year, 4) && !div(this.year, 100)
  }
}


module.exports = Year
