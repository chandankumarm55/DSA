'''
You are given two integers red and blue representing the count of red and blue colored balls.
You have to arrange these balls to form a triangle such that the 1st row will have 1 ball, 
the 2nd row will have 2 balls, the 3rd row will have 3 balls, and so on.

All the balls in a particular row should be the same color, and adjacent rows should have different colors.
Input: red = 2, blue = 4
Output: 3
Two Possiblity : we can start with red ball at frist line or we can start with blue ball at frist line 
so , we have call the helper function both the times , frist time using red ball at frist line another time we need call using 
blue ball at the frist time 
return max(self.helperFunction(red,blue), self.helperFunction(blue,red)) we need to return the maximum 
'''
class Solution(object):
    def maxHeightOfTriangle(self, red, blue):
        return max(self.helperFunction(red,blue), self.helperFunction(blue,red))
    
    def helperFunction(self,red , blue):
        h = 0
        i = 1
        while True:
            if i % 2 ==1:
                if red >= i:
                    red-=i
                else :
                    break
            else :
                if blue >= i:
                    blue -=i
                else :
                    break
            h+=1
            i+=1
        return h
