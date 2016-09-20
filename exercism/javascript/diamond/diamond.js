
const toOrd = ch => ch.charCodeAt(0)
const toAscii = n => String.fromCharCode(n)

class Diamond {
  makeDiamond(ch) {
    if (ch == 'A') return 'A\n'

    const prior = this.makeDiamond(toAscii(toOrd(ch) - 1)).split('\n')
    const top = prior.slice(0, prior.length / 2).map(str => ` ${str} `)
    const middle = ch + Array(top[0].length - 1).join(' ') + ch
    const bottom = top.slice().reverse()
    return top.concat(middle, bottom, '').join('\n')
  }
}

module.exports = Diamond
