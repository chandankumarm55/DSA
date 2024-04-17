"""
Maximun depth of a string
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.

"""

class Solution(object):
    def maxDepth(self, s):
        max_depth =0
        current_depth=0
        for char in s:
            if char == '(':
                current_depth+=1
                max_depth=max(max_depth,current_depth)
            elif char == ')':
               current_depth-=1
        return max_depth
s="(1)+((2))+(((3)))"
solution= Solution()
ans = solution.maxDepth(s)
print(ans)
                    