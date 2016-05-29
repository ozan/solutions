const BaseMatrix = require('../matrix/matrix')

const max = (xs) => Math.max.apply(null, xs)
const min = (xs) => Math.min.apply(null, xs)

function* genSaddlePoints ({rows, columns}) {
  for (let i = 0; i < rows.length; i++) {
    const row = rows[i]
    for (let j = 0; j < row.length; j++) {
      const x = row[j]
      if (x === max(row) && x === min(columns[j])) {
        yield [i, j]
      }
    }
  }
}

class Matrix extends BaseMatrix {
  constructor (args) {
    super(args)
    this.saddlePoints = Array.from(genSaddlePoints(this))
  }
}

module.exports = Matrix
