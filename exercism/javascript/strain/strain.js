
const keep = (xs, f) =>
  xs.reduce((memo, x) => f(x) ? (memo.push(x) && memo) : memo , [])

const discard = (xs, f) =>
  keep(xs, (x) => !f(x))

module.exports = { keep, discard }
