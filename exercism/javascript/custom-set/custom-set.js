
const all = (f, xs) =>
  Array.from(xs).every(f)

class CustomSet {
  constructor (valArray) {
    this.vals = new Set(valArray)
  }
  eql (other) {
    const [xs, ys] = [this.vals, other.vals]
    return xs.length === ys.length && all(x => ys.has(x), xs)
  }
  delete (val) {
    this.vals.delete(val)
    return this
  }
  empty () {
    return new CustomSet()
  }
  member (x) {
    return this.vals.has(x)
  }
  put (x) {
    this.vals.add(x)
    return this
  }
  size () {
    return this.vals.size
  }
  toList () {
    return Array.from(this.vals.values())
  }
  _relation (f) {
    return new CustomSet(this.toList().filter(f))
  }
  difference (other) {
    return this._relation(v => !other.vals.has(v))
  }
  intersection (other) {
    return this._relation(v => other.vals.has(v))
  }
  disjoint (other) {
    return this.intersection(other).size() === 0
  }
  subset (other) {
    return other.difference(this).size() === 0
  }
  union (other) {
    return new CustomSet(this.toList().concat(other.toList()))
  }
}

module.exports = CustomSet
