class Solution(object):
    def numSpecial(self, mat):
        row=len(mat)
        col=len(mat[0])
        count=0
        for i in range(row):
            for j in range(col):
                if mat[i][j]==1:
                    if sum(mat[i])==1 and sum(mat[k][j] for k in range(row))==1:
                        count+=1
        return count
        
        
