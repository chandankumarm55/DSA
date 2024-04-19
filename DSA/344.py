'''Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]'''



class Solution(object):
    def reverseString(self,s):
        left=0
        right=len(s)-1
        while left <right:
            s[left],s[right] = s[right],s[left]
            right-=1
            left+=1
        return s
