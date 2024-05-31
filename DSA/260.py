'''
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

we solve this problem by using simple steps 
step1 : find the Counter function for given nums which retruns the key as value of the item in nums and  value as how many times 
it present in list 
in this case it will be  counter = ({1:2,2:2,3:1,5:1})
step 2 :next iterate over the dictionary usinf items() function and find the if the val ==1 then addthe ley of the pair to the 
result list 
at the end of the iteration it will looks like result =[3,5]
step3:finally retrun the result
'''
import collections
class Solution(object):
    def singleNumber(self, nums):
        count=collections.Counter(nums)
        result=[]
        len(count)
        print(count)
        for key , val in count.items():
            if val==1:
                result.append(key)
        return result
