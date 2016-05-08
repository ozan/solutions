
const isLower = (char) => char.match(/[a-z]/)
const isUpper = (char) => char.match(/[A-Z]/)
const isAlpha = (char) => isLower(char) || isUpper(char)

const acronym = ({ res, prior }, char) => {
  if (prior === null ||
      !isAlpha(prior) && isAlpha(char) ||
      isLower(prior) && isUpper(char)) {
    res = res.concat(char.toUpperCase())
  }
  return { res, prior: char }
}

const parse = (phrase) =>
  phrase.split('').reduce(acronym, { res: '', prior: null }).res

module.exports = { parse }
