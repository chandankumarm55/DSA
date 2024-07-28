'''
Time complixity = o(z+(R+C) where z is the zero element in the lists and r is the rows in the matrix and c is the column in matrix
space complexity = o(z) 

Solution :
step 1 : declare row and col and zeroElementindexes 
step 2 :use i and j loop to find the indexes of matrix which has value of 0 
step 3 : then append the indexes of zero element of the matrix
step 4 : then again iterate in the matrix based on length of zeroElementindexes , and again 
assign the value of 0 to entire row and entire column 
'''
class Solution:
    def setZeroes(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        zeroElementindexes=[]

        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    zeroElementindexes.append([i,j])
        for i , j in zeroElementindexes:
            for k in range(col):
                matrix[i][k]=0
            for m in range(row):
                matrix[m][j] =0
        return matrix
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
solution = Solution()
print(solution.setZeroes(matrix))
