'''
Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

we can use backtracking and recursion technique to solve this problem
we have 2 helper function name palindrome and backtrack  
palidrome function is used to check whether the substring is paalidrome or not 
backtrack is called recursively to generate all possible subset 
'''

class Solution(object):
    def partition(self, s):
        result = []
        def palindrome(s):
            return s==s[::-1]
        def backtrack(start,path):
            if start ==len(s):
                result.append(path)
                return 
            for end in range(start+1,len(s)+1):
                substring=s[start:end]
                if palindrome(substring):
                    backtrack(end,path+[substring])
        backtrack(0,[])
        return result
                

