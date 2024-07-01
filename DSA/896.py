'''
Input: arr = [2,6,4,1]
Output: false

Explanation: There are no three consecutive odds.
we need retrun true if the nums array is monotonic , An array is monotonic if it is either monotone increasing or monotone
decreasing
so we need to sorted array in acccesding and decreasing order , if the num is equal either of one then  we will return true other
wise we retrun false

'''
class Solution(object):
    def isMonotonic(self, nums):
        sorted_increasing = sorted(nums)
        sorted_decreasing = sorted_increasing[::-1]

        if nums == sorted_increasing or nums == sorted_decreasing:
            return True
        else :
            return False
        
