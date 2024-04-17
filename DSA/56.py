class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])  # Sort intervals based on the start time
        merged = []
        
        for interval in intervals:
            # If the list of merged intervals is empty or if the current interval does not overlap with the previous,
            # simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # If there is an overlap, merge the current and previous intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

solution = Solution()
intervals = [[1, 4], [0, 0]]
ans = solution.merge(intervals)
print(ans)
