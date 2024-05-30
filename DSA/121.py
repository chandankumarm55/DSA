'''
We can solve this probelm by using simple steps 
problem = we need to find the maximum profit from an array of prices 
step 1 : if prices is emoty we will return 0
step 2: we assign the frist element of the prices array as min_price and max_profit as 0
step3: we iterate over the prices list and we will find the min_prices od stock that we can buy and also max_profit we can get 
by seeling . 
step 4: return max_profit
'''
class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit

prices = [7, 1, 5, 3, 6, 4]
solution = Solution()
result = solution.maxProfit(prices)
print("Maximum Profit =", result)
