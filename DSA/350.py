'''
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 
'''
class Solution(object):
    def intersect(self, nums1, nums2):
        nums1_dic = Counter(nums1)
        nums2_dic = Counter(nums2)
        result =[]

        for key , val in nums1_dic.items():
            if key in nums2_dic.keys():
                minimum = min(nums1_dic[key] , nums2_dic[key])
                for i in range(minimum):
                    result.append(key)
        return result
