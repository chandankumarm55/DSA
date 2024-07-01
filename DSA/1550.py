'''
we have return the tru if  the array have three consecutive odd number ,
count tracks the current count and final count hold the maximum consecutive oddd number 

'''
class Solution(object):
    def threeConsecutiveOdds(self, arr):
        count = 0
        final_count=0
        for i in range(len(arr)):
            if arr[i] % 2 !=0:
                count+=1
            else :
                count =0
            final_count = max(final_count , count)
        return final_count >=3
solution = Solution()
arr = [1,2,34,3,4,5,7,23,12]
ans = solution.threeConsecutiveOdds(arr)
# True
print(ans)
