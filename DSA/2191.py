'''
Input: mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38]
Output: [338,38,991]

time complexity = o(n log n)
space complexity = o(n)

step 1 :  mapping_array =[] is used to track the mapped value of the nums 
step 2 : itereate over nums array and store the current nums as in currrent varible as string type to making indexing in future
next , iterate over the current value of string numbers and accesse the mapping index and store in val varible and after 
this for loop add the val in to mapping_array as integer 
stp3 : then create counter varible for storing the zip dict of nums and mapping_array
step4 : sort the counter based on 1 index value in mapping_val that is value of index 
step 5 : next store the key value of sorted_items  and store in ans then return ans 

'''
class Solution:
    def sortJumbled(self, mapping, nums):
        #creating map array
        mapping_array =[]
        for i in range(len(nums)):
            current=str(nums[i])
            val=''
            for i in range(len(current)):
                val+=str(mapping[int(current[i])])
            mapping_array.append(int(val))
        print(mapping_array)
        # next zip the nums and mapping array to sort
        counter = zip(nums,mapping_array)
        sorted_items=sorted(counter , key=lambda x:x[1], reverse=False)
        ans=[key for key,_ in sorted_items]
        return ans
            
solution = Solution()
mapping =[8,9,4,0,2,1,3,5,7,6]
nums = [991,338,38]
ans = solution.sortJumbled(mapping,nums)
