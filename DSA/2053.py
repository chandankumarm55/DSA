'''
example : 
Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned. 

Time Complexoity : O(n)
step1: initialize the unique list for storing the unique array , and counter for creating a hash map for frequency
step2: iterate over the arr and check if the counter[string] is equal to 1 , if it is one meand then we can say that
the string char only onces in the arr list . if we found we need to add it to unique array 
step3 : next check if the length of unique is less then the k value if it true we need to return empty string 
step 4 : we need to return the k-1 index as our output 
'''
from collections import Counter
class Solution(object):
    def kthDistinct(self, arr, k):
        unique = []
        counter = Counter(arr)
        for string in arr: 
            if counter[string] == 1:
                unique.append(string)
        if len(unique) < k:
            return ''
        return unique[k-1]
