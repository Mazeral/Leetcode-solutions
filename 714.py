class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = -prices[0]
        for price in prices:
            # To actually understand the problem:
            # https://www.youtube.com/watch?v=OVsAAgy6awk
            new_cash = max(cash, hold + price - fee)
            new_hold = max(hold, cash - price)
            cash = new_cash
            hold = new_hold
        return cash
