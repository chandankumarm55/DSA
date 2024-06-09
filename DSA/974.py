'''
Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:

Input: nums = [5], k = 9
Output: 0
we can solveg this using maps 
 step1:remainder_count to store the remainder and cumlative_sum is for storing the sum of items
 step2:iterate the nums array and find the cumulative count and find the remainder of that cumulative_sum 
 step3: if the remiander is already in the remainder_count map means that the sub array is devisible by k
 and add the count by remainder-count[remiander] and remainder_count{remiander] by one 
 else:
 assign the remiander_count[remiander] =1

 time complixity = o(n)
'''

class Solution(object):
    def subarraysDivByK(self, nums, k):
        remainder_count = {0: 1}  
        cumulative_sum = 0
        count = 0
        
        for num in nums:
            cumulative_sum+=num
            remainder=cumulative_sum%k
            

            if remainder in remainder_count:
                count+=remainder_count[remainder]
                remainder_count[remainder]+=1
            else:
                remainder_count[remainder]=1
        return count
