'''
Input: nums = [1,2,3]
Output: [1,3,2]

step1: find the frist decreasing element in array means while return false for below condition 
 i=len(nums)-2
        while i >= 0 and (nums[i]>=nums[i+1]):
            i-=1
step2:then if the val of the i not equal to -1 then we will find the rightmost largest element and swap the nums[j] and nums[i]
then finallay we will reverse the nums[i+1] index to till the end of the array 
'''
class Solution(object):
    def nextPermutation(self, nums):
        i=len(nums)-2
        while i >= 0 and (nums[i]>=nums[i+1]):
            i-=1
        if i!=-1:
            j=len(nums)-1
            while j>=0 and (nums[j]<=nums[i]):
                j-=1
            nums[i],nums[j] =nums[j],nums[i]
        nums[i+1:] = reversed(nums[i+1:])
