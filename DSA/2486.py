'''
s ="vrykt"
t ="rkge"
Output =  2
Expected = 2

The problem states that we have to find the number of charater we need to make the substring of t where all the charater in the 
t is present in the string s 

step 1 : create a varible for keeping track of indexes of t and s 
step2: create while loop for iterating the string of both the string s and t 
if the charter present in the string t then we increament the value of the t_index and here we will know the how many charter 
are present in the string t , in the above trst case r,k are present in the string t 
step 3: we retrun the length of the string t - t_index value , in this case the t_index value will be 2 and length pf the string is 
4 so then anwer will be 4-2 which is equall to 2
'''


class Solution(object):
    def appendCharacters(self, s, t):
        t_index = 0
        s_index = 0
        
        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                t_index += 1
            s_index += 1
        
        return len(t) - t_index
