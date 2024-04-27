'''
Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1'''


class Solution:
    def numberOfSubstrings(self, s):
        counts = {'a': 0, 'b': 0, 'c': 0}
        start = end = 0
        result = 0
        
        while end < len(s):
            # Expand the window
            counts[s[end]] += 1
            end += 1
            
            # Shrink the window until all characters are present
            while all(counts.values()):
                counts[s[start]] -= 1
                start += 1
                
            # Update result
            result += start
            
        return result

# Example usage:
solution = Solution()
s = "abcabc"
print(solution.numberOfSubstrings(s))  # Output: 10
