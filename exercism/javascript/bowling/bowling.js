
_score = ({ throws=0, frame=1, prior=0, bonus=0, nextBonus=0, total=0, fill}, x) => {
  const strike = x == 10 && throws == 0
  const spare = x + prior >= 10
  const final = frame == 10
  const over = final ? (throws == 2 || throws == 1 && !spare) : (strike || throws == 1)


  if (x < 0 || x > 10)
    throw new Error('Pins must have a value from 0 to 10')
  if (x + prior > 10 && !fill)
    throw new Error('Pin count exceeds pins on the lane')
  if (frame > 10)
    throw new Error('Should not be able to roll after game is over')

  return {
    throws: over ? 0 : throws + 1,
    frame: frame + over,
    prior: over ? 0 : x,
    bonus: nextBonus + (spare && !final),
    nextBonus: 0 + (strike && !final),
    total: total + (1 + bonus) * x,
    fill: fill || (final && spare)
  }
}



class Bowling {
  constructor (rolls) {
    this.rolls = rolls
  }
  score () {
    const result = this.rolls.reduce(_score, {})

    if (!result.frame || result.frame < 11)
      throw new Error('Score cannot be taken until the end of the game')

    return result.total
  }
}

module.exports = Bowling
