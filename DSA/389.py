'''
Input: s = "abcd", t = "abcde"
Output: "e"
Problem is : we have to find the missing alphabets which is not present the string t and with the count also 
approch = we can use two hash map or dictinary for storing the occurence of the element 
i.e 
Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1})
Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1})
we can see the char e is not present in the s string 
then  we will iterate over the counted_t with items() this will make sure the both key and value are iterating 
i.e dict_items([('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1)])
condition : if counted_t[key]!=counted_s[key]:
                count=counted_t[key]-counted_s[key]
                missed+=key*count
if the key of the counted_t is not equal to counted_s then we have to find the how many char is differnt 
then we will increment the missed value by particular char
finally we retrun the missed char
'''
class Solution(object):
    def findTheDifference(self, s, t):
        counted_t =Counter(t)
        counted_s=Counter(s)
        missed = ''
        for key , val in counted_t.items():
            if counted_t[key]!=counted_s[key]:
                count=counted_t[key]-counted_s[key]
                missed+=key*count
        return missed
        
                
