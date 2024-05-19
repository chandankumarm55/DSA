'''
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
step 1:sort the points array with key of 2nd element of the 2d array that is [1]
step 2:assign the valu of current_position = points[0][1] in this case it will be 6
step3:iterate over the points list and if the start > current_position then will increment the arrow count
and will shift the current_position value = end
'''
class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key=lambda x:x[1])
        if not points:
            return
        arrow=1
        current_position=points[0][1]
        for start, end in points:
            if start > current_position:
                arrow+=1
                current_position=end
        return arrow
