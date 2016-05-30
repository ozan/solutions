
const ascending = (xs) =>
  xs.reduce(([b, x], y) => [b && x <= y, y], [true, -Infinity])[0]

class BinarySearch {
  constructor (xs) {
    if (ascending(xs)) this.array = xs
  }
  indexOf (x) {
    let [i, j] = [-1, this.array.length]
    while (i < j) {
      const mid = Math.floor((i + j) / 2)
      const probe = this.array[mid]
      if (x === probe) return mid
      if (x < probe) {
        j = mid - 1
      } else {
        i = mid + 1
      }
    }
    return -1
  }
}

module.exports = BinarySearch
