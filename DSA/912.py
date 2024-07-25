'''
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.

 time_complexity = O(n+k) where n is number of elements and k is size of range of element in the nums array
 space_comlexity = o(n)
 
pigeonhole_sort : 
step 1 : find the min and max val in  and find the size using size = max_val - min_val + 1 
step 2 :  next create a empty [] list in array 
step 3 : next iterate on the arr list and append the element to num - min_val index 
step 3 : next iterate on array list and remove the [] list brackets from array and remove the empty list and store it in
result 
step 4 : return  the result list 
 
'''
class Solution:
    def sortArray(self, arr):
        min_val = min(arr)
        max_val = max(arr)
        size=max_val - min_val +1 
        array=[[] for _ in range(size)]
        for num in arr:
            array[num-min_val].append(num)
        result=[]
        for num in array:
            result.extend(num)
        return result
