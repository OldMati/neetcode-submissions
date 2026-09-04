class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        holding = prices[0] # want to hold as low price as possible and sell as high as possible

        for price in prices[1:]:
            if price > holding:
                profit += price - holding
                holding = price
            else:
                holding = min(holding, price)
        
        return profit
        