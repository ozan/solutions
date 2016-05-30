
const syms = {
  '(': ')',
  '{': '}',
  '[': ']'
}

const isBalanced = (str) => {
  const stack = []
  for (let char of str) {
    if (syms[char]) {
      stack.push(char)
      continue
    }
    const top = stack.pop()
    if (syms[top] !== char) return false  // mismatch or right-heavy
  }
  return stack.length === 0  // false if left-heavy
}

module.exports = isBalanced
