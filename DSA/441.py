'''You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

 '''

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Initialize variables to keep track of the current number of coins and rows
        coins = 0
        rows = 0
        
        # Iterate through each row until there are no more coins left
        while n >= coins + rows + 1:
            rows += 1
            coins += rows
        
        return rows

# Test cases
solution = Solution()
print(solution.arrangeCoins(5))  # Output: 2
print(solution.arrangeCoins(8))  # Output: 3
