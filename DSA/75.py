"""this is the one of the sorting technique called selection sort """


class Solution(object):
    def sortColors(self, nums):
        n=len(nums)
        for i in range(n):
            for j in range(i,n):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        return nums
            
nums=[2,0,2,1,1,0]
solution=Solution()
ans=solution.sortColors(nums)  
print(ans)
    
