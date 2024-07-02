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
