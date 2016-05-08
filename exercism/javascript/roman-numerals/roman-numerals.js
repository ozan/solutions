
const parts = [
  [1000, 'M'],
  [900, 'CM'],
  [500, 'D'],
  [400, 'CD'],
  [100, 'C'],
  [90, 'XC'],
  [50, 'L'],
  [49, 'IL'],
  [40, 'XL'],
  [10, 'X'],
  [9, 'IX'],
  [5, 'V'],
  [4, 'IV'],
  [1, 'I']
]

const toRoman = (arabic) => {
  if (arabic === 0) return ''
  const [sub, roman] = parts.filter(([n, _]) => n <= arabic)[0]
  return `${roman}${toRoman(arabic - sub)}`
}

module.exports = toRoman
