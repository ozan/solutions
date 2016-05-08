
module.exports = (xs, f) =>
  xs.reduce((memo, x) => (memo.push(f(x)) && memo), [])
