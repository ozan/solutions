const floorDiv = (n, d) => Math.floor(n / d)
const minsInDay = 60 * 24
const twoP = (n) => n < 10 ? `0${n}` : `${n}`


class Clock {
  constructor (mins) {
    this.mins = mins
  }
  plus (dMins) {
    return new Clock((minsInDay + this.mins + dMins) % minsInDay)
  }
  minus (dMins) {
    return this.plus(-dMins)
  }
  toString () {
    const [hours, mins] = [floorDiv(this.mins, 60), this.mins % 60]
    return `${twoP(hours)}:${twoP(mins)}`  // TODO leading 0
  }
  equals (other) {
    return this.mins === other.mins
  }
}

const at = (hours, minutes=0) => new Clock(hours * 60 + minutes)

module.exports = { at }
