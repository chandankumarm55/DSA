'''
Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

'''
class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        deff = True
       
        defferece = arr[1]-arr[0]
        
        for i in range(1,len(arr)):
            if arr[i] - arr[i-1] != defferece :
                deff = False
                
        return deff
arr = [3,5,1]
solution =Solution()
ans = solution.canMakeArithmeticProgression(arr)
print(ans)
