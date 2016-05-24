class Node {
  constructor (val) {
    this.val = val
    this.prior = null
    this.next = null
  }
}


class LinkedList {
  constructor () {
    this.head = null
    this.tail = null
  }
  push (val) {
    const n = new Node(val)
    if (this.head) {
      this.head.prior = n
      n.next = this.head
      this.head = n
    } else {
      this.head = n
      this.tail = n
    }
  }
  pop () {
    const n = this.head
    this.head = this.head.next
    if (this.head) {
      this.head.prior = null
    }
    if (this.tail === n) {
      this.tail = null
    }
    return n.val
  }
  shift () {
    const n = this.tail
    this.tail = this.tail.prior
    if (this.tail) {
      this.tail.next = null
    }
    if (this.head === n) {
      this.head = null
    }
    return n.val
  }
  unshift (val) {
    const n = new Node(val)
    if (this.tail) {
      this.tail.next = n
      n.prior = this.tail
      this.tail = n
    } else {
      this.head = n
      this.tail = n
    }
  }
  count () {
    let n = this.head
    let count = 0
    while (n) {
      count ++
      n = n.next
    }
    return count
  }
  delete (val) {
    let [m, n] = [null, this.head]
    while (n) {
      if (n.val === val) {
        if (m) {
          m.next = n.next
          m.next.prior = m
        } else {
          this.head = n.next
          if (n.next) n.next.prior = null
        }
        return
      }
      [m, n] = [n, n.next]
    }
  }
}

module.exports = LinkedList
