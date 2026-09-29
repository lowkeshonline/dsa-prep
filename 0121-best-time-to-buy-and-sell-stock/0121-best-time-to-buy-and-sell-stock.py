class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        max_profit = 0
        buy = 0
        sell = 1
        
        while (sell < len(prices)):

            if prices[buy] < prices[sell]:
                curr_profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, curr_profit)
            else:
                buy = sell

            sell += 1
        
        return max_profit
