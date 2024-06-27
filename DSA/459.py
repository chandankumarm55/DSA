'''
Concatenate the String with a Shift:
it will ba done by add the s without frist charater  and also add the substring from last to frist in reverse order without 
adding the last element i.e 
s_subtring = baba
if the we can can the string s by s_subtring it will retrun true other wise it will return false

'''


class Solution(object):
    def repeatedSubstringPattern(self, s):
        s_substring =''.join((s[1:],s[:-1]))
        return s in s_substring
solution =Solution()
s = "aba"
ans = solution.repeatedSubstringPattern(s)
print(ans)
