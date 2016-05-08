const allergies = 'eggs peanuts shellfish strawberries tomatoes chocolate pollen cats'.split(' ')


class Allergies {
  constructor (score) {
    this.allergens = allergies.filter((_, i) => (1 << i & score) > 0)
  }
  list () {
    return this.allergens
  }
  allergicTo (thing) {
    return this.allergens.includes(thing)
  }
}

module.exports = Allergies
