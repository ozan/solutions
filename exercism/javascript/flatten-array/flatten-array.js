
const flattenUnit = (a) =>
  a instanceof Array ? flattenArray(a) : a === null ? [] : [a]

const flattenArray = ([head, ...rest]) => {
  if (head === undefined) return []
  return flattenUnit(head).concat(flattenArray(rest))
}

class Flattener {
  flatten (arr) {
    return flattenArray(arr)
  }
}

module.exports = Flattener
