const { identity, mapValues, sortBy } = require('lodash/fp')


class School {

  constructor () {
    this._roster = {}
  }

  add (name, grade) {
    this._roster[grade] = this._roster[grade] || []
    this._roster[grade].push(name)
  }

  roster () {
    return mapValues(sortBy(identity), this._roster)
  }

  grade (n) {
    return this.roster()[n] || []
  }

}

module.exports = School
