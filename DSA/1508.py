'''
If you don't use the modulo operation, the sum can become very large, causing overflow or integer limits issues in
some programming environments (though Python handles large integers well).

 i didnt used modole opertation so i got this test case error 
53/54 Use Testcase
Output
16716700000
Expected
716699888

to handle the large numbers we need to use modle operation
'''
class Solution(object):
    def rangeSum(self, nums, n, left, right):
        sum_array = []
        length = len(nums)
        
        for i in range(length):
            current_sum = 0
            for j in range(i, length):
                current_sum += nums[j]
                sum_array.append(current_sum)
        
        sum_array.sort()
        mod = 10**9 + 7
        return sum(sum_array[left - 1 : right]) % mod
        
        return required_sum

solution = Solution()
nums = [1, 2, 3, 4]
n = 4
left = 1
right = 5
ans = solution.rangeSum(nums, n, left, right)
print(ans)
