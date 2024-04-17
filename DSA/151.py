'''Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.'''

class Solution(object):
    def reverseWords(self, s):
        splitted=s.split()
        reversed_string = ' '.join(splitted[::-1])
        return reversed_string
s = "a good   example"
solution=Solution()
calling=solution.reverseWords(s)
        
        