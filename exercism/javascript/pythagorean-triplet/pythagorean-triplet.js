const sq = (n) => n * n

class Triplet {
  constructor (a, b, c) {
    this.a = a
    this.b = b
    this.c = c
  }
  sum () {
    return this.a + this.b + this.c
  }
  product () {
    return this.a * this.b * this.c
  }
  isPythagorean () {
    return sq(this.a) + sq(this.b) === sq(this.c)
  }
}

Triplet.where = ({ maxFactor, minFactor=1, sum}) => {
  const triplets = Array.from(genTriplets(minFactor, maxFactor))
  return sum ? triplets.filter(t => t.sum() === sum) : triplets
}

function* genTriplets (min, max) {
  for (let a=min; a <= max; a++) {
    for (let b=a+1; b <= max; b++) {
      const c = Math.sqrt(sq(a) + sq(b))
      if (c % 1 == 0 && c <= max) {
        yield new Triplet(a, b, c)
      }
    }
  }
}


module.exports = Triplet
