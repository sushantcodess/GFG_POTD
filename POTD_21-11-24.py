class Solution:
    def maximumProfit(self, prices):
        n = len(prices)
        if n  < 2:
            return 0
        ans = 0
        run = 0
        for i in range(1,n):
            run = max(0,run + prices[i] - prices[i-1])
            ans = max(ans , run)
        return ans