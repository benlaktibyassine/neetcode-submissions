class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        maxP=0
        profit=0
        while r<len(prices):
            if prices[r]-prices[l]<0:
                l=r
                r+=1
                profit=0
            else:
                profit=prices[r]-prices[l]
                maxP=max(profit,maxP)
                r+=1
        return maxP