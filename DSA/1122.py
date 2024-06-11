'''
Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

step 1 : count the occurence of each num in aarr1
step 2 : iterate the arr2 and if the num in arr1 also then append the num how many time in arr1 
using the value of the count_map[num]
step3: delete the count_map[num] in each iteration , becuase to know which didnt append for result
step4 : append the remaining count by sorting the keys of the count_map
step 5 : return the result list
'''

class Solution:
    def relativeSortArray(self,arr1, arr2):
        count_map =Counter(arr1)
        result=[]
        
        for num in arr2:
            if num in arr1:
                result.extend([num]*count_map[num])
                del count_map[num]
        for num in sorted(count_map.keys()):
            result.extend([num]*count_map[num])
        return result

        
