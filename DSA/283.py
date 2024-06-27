'''
Problem we have to move the zero in nums array to the end of the nums array , we need to change the orginal array only we
should not create any dummy or copy
step1 : initailize the zer o variable to keep tract of non zero element 
step 2 : iterate iver the nums array and check if the nums[i] is not 0
atep 3 : if the nums [i] not zero then we will swap the i index eith zero index 
and increment the zero
time complexity is o(n)
'''
class Solution(object):
    def moveZeroes(self, nums):
        length=len(nums)
        zero=0
        for i in range(length):
            if nums[i]!=0:
                nums[i] , nums[zero] = nums[zero] , nums[i]
                zero+=1
        return nums
            
