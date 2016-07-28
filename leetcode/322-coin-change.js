var coinChange = function (coins, amount) {
  var memo = Array(amount + 1).fill(amount + 1)
  memo[0] = 0
  for (var i=0; i < coins.length; i++) {
    var coin = coins[i]
    for (var j=coin; j <= amount; j++) {
      memo[j] = Math.min(memo[j], memo[j - coin] + 1)
    }
  }
  return memo[amount] > amount ? -1 : memo[amount]
}
