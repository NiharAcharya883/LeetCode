from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        l = len(prices)
        for i in range(l):
            for j in range(i,l):
                if j>i and prices[j]<=prices[i]:
                    prices[i] = prices[i] - prices[j]
                    break
        return prices