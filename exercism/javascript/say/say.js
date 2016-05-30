
const parts = [
  [1e9, 'billion'],
  [1e6, 'million'],
  [1e3, 'thousand'],
  [100, 'hundred'],
  [90, 'ninety'],
  [80, 'eighty'],
  [70, 'seventy'],
  [60, 'sixty'],
  [50, 'fifty'],
  [40, 'forty'],
  [30, 'thirty'],
  [20, 'twenty'],
  [19, 'nineteen'],
  [18, 'eighteen'],
  [17, 'seventeen'],
  [16, 'sixteen'],
  [15, 'fifteen'],
  [14, 'fourteen'],
  [13, 'thirteen'],
  [12, 'twelve'],
  [11, 'eleven'],
  [10, 'ten'],
  [9, 'nine'],
  [8, 'eight'],
  [7, 'seven'],
  [6, 'six'],
  [5, 'five'],
  [4, 'four'],
  [3, 'three'],
  [2, 'two'],
  [1, 'one'],
  [0, 'zero']
]

const floorDiv = (x, y) => Math.floor(x / y)

const say = (n, prefix) => {
  const [part, name] = parts.filter(([part, name]) => part <= n)[0]
  const [high, low] = [floorDiv(n, part), n % part]
  const tailPrefix = part < 100 ? '-' : ' '
  const tail = low > 0 ? say(low, tailPrefix) : ''

  if (part < 100) return `${prefix}${name}${tail}`

  const head = say(high, prefix ? ' ' : '')
  return `${head} ${name}${tail}`
}

const inEnglish = (n, prefix='') => {
  if (n < 0 || n >= 1e12) throw 'Number must be between 0 and 999,999,999,999.'
  return say(n, prefix)
}

module.exports = { inEnglish }
