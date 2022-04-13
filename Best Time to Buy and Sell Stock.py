class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        min_buy=prices[0]
        for idx in range(len(prices)):
            min_buy=min(prices[idx],min_buy)
            profit=max(profit,prices[idx]-min_buy)
        return profit

        