const { split, map, spread, chunk, flatten, get, flow, zip } = _ = require('lodash/fp')

const defaultStudents = [
    'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet',
    'Ileana', 'Joseph', 'Kincaid', 'Larry'
]

const plantNames = {
  G: 'grass',
  C: 'clover',
  R: 'radishes',
  V: 'violets'
}

const plantsForConfig = flow(
  split('\n'),
  map(split('')),
  spread(zip),
  chunk(2),
  map(spread(zip)),
  map(flatten),
  map(map(get(_, plantNames)))
)

class Garden {
  constructor (config, students) {
    const plants = plantsForConfig(config)
    students = (students || defaultStudents).sort()
    for (let i = 0; i < plants.length; i++) {
      this[students[i].toLowerCase()] = plants[i]
    }
  }
}

module.exports = Garden
