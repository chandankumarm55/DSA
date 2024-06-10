''' Problem example 
Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.

 step 1 : we should solve the given array and store it in sorted_heights variable 
 step2 : and next iterate on both the sorted_heights and heights and check if the both value at position is same if not 
 increase the count by 1 
 step 3 : retrun the count 

 time complexity of this program is o(n)

'''

class Solution(object):
    def heightChecker(self, heights):
        length = len(heights)
        count=0
        sorted_heights=sorted(heights)
        for i in range(length):
            if not heights[i] == sorted_heights[i]:
                count+=1
        return count
