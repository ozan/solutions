var maxProfit = function(prices) {
  if (prices.length < 2) return 0
  var sell = 0
  var buy = -prices[0]
  var prev_sell = 0
  var prev_buy = 0
  for (var i = 0; i < prices.length; i++) {
    var price = prices[i]
    prev_buy = buy
    buy = Math.max(prev_sell - price, prev_buy)
    prev_sell = sell
    sell = Math.max(prev_buy + price, prev_sell)
  }
  return sell
};
