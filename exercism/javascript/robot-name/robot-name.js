
const alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
const num = '0123456789'
const randChoice = (xs) => xs[Math.floor(xs.length * Math.random())]


class Robot {
  constructor () {
    this.reset()
  }

  reset () {
    const name = this.randomName()
    if (Robot.globallyKnownNames.has(name)) return this.reset()
    Robot.globallyKnownNames.add(name)
    this.name = name
  }

  randomName () {
    return [alpha, alpha, num, num, num].map(randChoice).join('')
  }
}

Robot.globallyKnownNames = new Set()

module.exports = Robot
