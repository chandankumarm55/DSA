class Solution(object):
    def spiralOrder(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        result = []
        top = 0
        left = 0
        right = col - 1
        bottom = row - 1
        
        while left <= right and top <= bottom:
            # Traverse top row
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1
            
            # Traverse right column
            for j in range(top, bottom + 1):
                result.append(matrix[j][right])
            right -= 1
            
            # Traverse bottom row
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1
            
            # Traverse left column
            if left <= right:
                for j in range(bottom, top - 1, -1):
                    result.append(matrix[j][left])
                left += 1
        
        return result

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
solution = Solution()
ans = solution.spiralOrder(matrix)
print(ans)
