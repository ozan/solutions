
class Gigasecond {
  constructor (d) {
    this.d = d
  }
  date () {
    return new Date(this.d.getTime() + 1e12)
  }
}

module.exports = Gigasecond
