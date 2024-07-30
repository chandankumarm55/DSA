'''
input : matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
output : 1 , 2 , 3, 4 , 8, 12 , 11 ,10 ,9 ,5 ,6 ,7

time complexity : O(r*c) where is the r is the number of row in the matrix and c is the columns in matrix
space complecity : O(1) 

approach : using indexing and slicing 
step 1 : declare a result list to store the answer 
step 2 : using while loop iterate on matrix 
step 3 : frist we need to append the frist row of the matrix  using this index matrix.pop(0)
step 4 : next we need to remove the right most element in each row so we need to use this index s and loop 
if matrix and matrix[0]:
                for row in matrix:
                    print(row[-1])
                    result.append(row.pop())
step 5 : next we need to remove the last row element so we need to reverse the element is it using  [::-1]
if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))
step 6 : lastly we need to iterate on 2 row that is noe frist roe in thr matrix after removing all the element 
so in order to remove the frist element frist we need to reverse the array
 if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))
step 7 : finally return result list 

''' 
class Solution(object):
    def spiralOrder(self, matrix):
        result = []
        count=1
        while matrix:
            # Add the first row to result
            result += matrix.pop(0)
          
            # Add the last element of each remaining row
            if matrix and matrix[0]:
                for row in matrix:
                    print(row[-1])
                    result.append(row.pop())
            
            
            # Add the last row (reversed) to result
            if matrix:
                result += matrix.pop()[::-1]
            print(result)
            
            # Add the first element of each remaining row (reversed order)
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))
        
        
        return result

# Example usage:
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(matrix)
solution = Solution()
ans = solution.spiralOrder(matrix)
print(ans)
