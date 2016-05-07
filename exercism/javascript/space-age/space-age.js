

const planetYears = [
  ['Earth', 1],
  ['Mercury', 0.2408467],
  ['Venus', 0.61519726],
  ['Mars', 1.8808158],
  ['Jupiter', 11.862615],
  ['Saturn', 29.447498],
  ['Uranus', 84.016846],
  ['Neptune', 164.79132]
]

const secondsPerYear = 31557600

const toTwo = (n) => Math.round(n * 1e2) / 1e2

class SpaceAge {
  constructor (seconds) {
    this.seconds = seconds
    planetYears.forEach(([planet, earthYears]) => {
      this[`on${planet}`] = () =>
        toTwo(seconds / (secondsPerYear * earthYears))
    })
  }
}

module.exports = SpaceAge
