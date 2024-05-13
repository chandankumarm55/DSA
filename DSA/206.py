'''
Frist we will split the s string and store it in list 
secondly we create a match dict for store the patters
thirdly we iterate the s_split and pattern , if pattter[i] not in match dict and current s_split is not in match.values() then
it means we dont have the pattern in match dic so we add that using match[pattern[i]]=s_list[i]
fouthly we check for any pattern failuer if current pattern not in match dict and patter[i] key is not equal to s_list then we retrun False
finnaly we return True
'''
class Solution(object):
    def wordPattern(self, pattern, s):
        s_list=list(s.split())
        print(s_list[0])
        match={}
        if len( s_list) != len(pattern):
            return False
        for i in range(len(pattern)):
            print(match)
            if pattern[i] not  in match  and s_list[i] not in match.values():
                match[pattern[i]]=s_list[i]
            elif pattern[i] not in match or match[pattern[i]] != s_list[i]:
                return False
        
        print()
        return True
