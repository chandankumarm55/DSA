'''
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.


'''
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        odd_matrix =False
        k=0
        total_sum=[]
        if len(mat)%2 !=0:
            odd_matrix =True
        for i in range(len(mat)):
            total_sum.append(mat[i][i])
        for j in range(len(mat)-1,-1,-1):
            total_sum.append(mat[k][j])
            k+=1
        if odd_matrix:
            intersection=len(mat)//2
            ans = sum(total_sum) - mat[intersection][intersection]
            return ans
        else :
            return sum(total_sum)
        
