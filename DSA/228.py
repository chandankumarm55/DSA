"""
fiding the range can don by using the below algorithm
frist we created ans list and initilized start and end to starting number 
second we iterate through array and if the previsouse number +1 and current number is not equal it means the given number are 
not in consective so we append the start and end number to the and list
we convert the end and start to str evey time because we want to present in -> like this we can add strings like this 

"""


class Solution:
    '''Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]'''
    def summaryRanges(self, nums):
        if not nums:return [] 
        ans = []
        start = end  = str(nums[0]) 
        for i in range(1 , len(nums)):
            if nums[i] != nums[i - 1] + 1:      

                if start != end:   
                    ans.append(start+'->'+end)
                else:
                    ans.append(start)
                start = end = str(nums[i])
            else:
                end = str(nums[i]) 
        if start != end:
            ans.append(start+'->'+end)
        else:
            ans.append(start)
        return ans
