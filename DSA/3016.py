'''
Example : 
Input: word = "abcde"
Output: 5
Explanation: The remapped keypad given in the image provides the minimum cost.
"a" -> one push on key 2
"b" -> one push on key 3
"c" -> one push on key 4
"d" -> one push on key 5
"e" -> one push on key 6
Total cost is 1 + 1 + 1 + 1 + 1 = 5.

Time Complexity : O(n) where n is number of element in the string 

problem statement : we have to find the number key pressed in the digital machine it allows us to modify the key as we want
means we can make 8 key as 1 press and remaining as 2 press and 3 press so one. 

solution :
step 1: next we need to initialze Counter variable for frequency 
step 2: initialze the ans variable  for storing the answer and val for keeping the multification whether the frequency shouldbe
multiply by 1 , 2 or 3
step 3 : next iterate on cnt counter and make sure u sorted the cnt counter based on the 2nd element of the counter varible 
next make multiply for 2nd element of the item and increa the val to keep the track of multification 
step 4 : if the val of the val is completly divide by 8 then we need to increase the val by one 
'''
from collections import Counter
class Solution:
    def minimumPushes(self, word):
        cnt = Counter(word)
        need = sorted(cnt.items(), key=lambda  x:x[1] ,reverse=True)
        print(need)
        ans = 0
        val = 1
        for i in range(len(cnt)):
            freq = need[i][1]
            ans+=freq*val
            if (i+1)%8==0:
                val+=1
        return ans
solution =Solution()
word = "aabbccddeeffgghhiiiiii"
ans = solution.minimumPushes(word)
print(ans)
