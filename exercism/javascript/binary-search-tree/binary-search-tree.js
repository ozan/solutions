
class BST {
  constructor (data) {
    this.data = data
  }
  insert (x) {
    const target = x <= this.data ? 'left' : 'right'
    if (this[target]) return this[target].insert(x)
    this[target] = new BST(x)
  }
  each (f) {
    if (this.isLeaf()) return f(this.data)
    this.left && this.left.each(f)
    f(this.data)
    this.right && this.right.each(f)
  }
  isLeaf () {
    return !(this.left || this.right)
  }
}

module.exports = BST
