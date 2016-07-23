class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        best_sell_price = 0
        best_profit = 0
        for price in reversed(prices):
            if price > best_sell_price:
                best_sell_price = price
            else:
                potential_profit = best_sell_price - price
                if potential_profit > best_profit:
                    best_profit = potential_profit
        return best_profit
