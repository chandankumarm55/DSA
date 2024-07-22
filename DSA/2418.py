'''
Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.

Time complixity = O(nlogn) and  space Complixity is O(n)

step 1 : we are ziping the names and heights as a tuple like key value pair 
step 2 : next we need to use sorted() built in function and ans we prople is the list we want to sort and 
we used lambda as key to sort based on some condition , here we used x:X[1] means we need to sort based on 2 value presents in 
people list 
step 3 : we need to iterate the sorted_prople and store the first element of sorted_people and retrun the ans 
'''

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = zip(names,heights)
        sorted_people = sorted(people , key= lambda x:x[1] , reverse=True)
        ans = [people for people,_ in sorted_people]
        return ans
