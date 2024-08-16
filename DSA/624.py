class Solution(object):
    def maxDistance(self, arrays):
        globalMin = arrays[0][0]
        globalMax = arrays[0][-1]

        max_distance = 0
        length = len(arrays)

        for i in range(1,length):
            currentMin = arrays[i][0]
            currentMax = arrays[i][-1]

            max_distance = max(max_distance , abs(currentMax - globalMin) , abs(globalMax - currentMin))
            globalMin = min(globalMin , currentMin)
            globalMax = max(globalMax , currentMax)
        
        return max_distance
