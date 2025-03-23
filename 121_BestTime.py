class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        maxprofit = 0

        for i in range(1, len(prices)):
            #If prices[i] is the best place to buy so far, update maxprofit  
            if prices[i] - lowest > maxprofit: 
                maxprofit = prices[i] - lowest
            
            #If prices[i] is the lowest number so far, update lowest
            if prices[i] < lowest:
                lowest = prices[i]

        return maxprofit
        