
const pourX  = ([x, X], [y, Y]) =>
  x + y > Y ? [x - (Y - y), Y] : [0, x + y]
const pourY  = ([x, X], [y, Y]) =>
  x + y > X ? [X, y - (X - x)] : [x + y, 0]
const emptyX = ([x, X], [y, Y]) => [0, y]
const emptyY = ([x, X], [y, Y]) => [x, 0]
const fillX  = ([x, X], [y, Y]) => [X, y]
const fillY  = ([x, X], [y, Y]) => [x, Y]

const actions = [pourX, pourY, emptyX, emptyY, fillX, fillY]

const key = ([a, b]) => `${a},${b}`

class TwoBucket {
  constructor (X, Y, goal, starter) {
    const initial = starter === 'one' ? [X, 0] : [0, Y]
    const q = [[initial, 1]]
    const seen = new Set([key(initial)])
    while (true) {
      const [[x, y], steps] = q.shift()
      if (x === goal && starter === 'one') {
        this.otherBucket = y
        this.moves = () => steps
        break
      }
      if (y === goal && starter === 'two') {
        this.otherBucket = x
        this.moves = () => steps
        break
      }
      for (let f of actions) {
        const res = f([x, X], [y, Y])
        if (!seen.has(key(res))) {
          seen.add(key(res))
          q.push([res, steps + 1])
        }
      }
    }
    this.goalBucket = starter
  }
}

module.exports = TwoBucket
