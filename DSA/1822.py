'''
Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1
time complixity is o(n)
'''
class Solution(object):
    def arraySign(self, nums):
        mul= 1
        for num in nums:
            mul*=num
        if mul > 0:
            return 1
        elif mul ==0:
            return 0
        else :
            return -1
