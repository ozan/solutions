
const bearings = 'north east south west'.split(' ')

const step = {
  north: [0, 1],
  east: [1, 0],
  south: [0, -1],
  west: [-1, 0],
}

const commands = {
  L: 'turnLeft',
  R: 'turnRight',
  A: 'advance',
}

class Robot {
  orient (bearing) {
    if (!new Set(bearings).has(bearing)) throw 'Invalid Robot Bearing'
    this.bearing = bearing
  }
  at (x, y) {
    this.coordinates = [x, y]
  }
  place ({x, y, direction}) {
    this.orient(direction)
    this.at(x, y)
  }
  turnRight () { this._turn(1) }
  turnLeft () { this._turn(-1) }
  _turn (delta) {
    const bi = bearings.indexOf(this.bearing)
    this.bearing = bearings[(4 + bi + delta) % 4]
  }
  advance () {
    const [dx, dy] = step[this.bearing]
    const [x, y] = this.coordinates
    this.coordinates = [x + dx, y + dy]
  }
  instructions (str) {
    return str.split('').map(ch => commands[ch])
  }
  evaluate (str) {
    this.instructions(str).forEach(instruction => this[instruction]())
  }
}

module.exports = Robot
