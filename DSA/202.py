'''
to find the happy number frist we use a while loop with True means we dono the ending 
we keep an seen set to see the cycle if the sum vakue came again we can return False 
if the sum vlue is 1 then we can retrun True 
if both didnt meet the condition we add the sum into seen set and n=sum for next iteration
'''


class Solution(object):
    def isHappy(self, n):
        seen=set()
        while True:
            sum=0
            while n >0:
                r=n%10
                sum+=r**2
                n//=10
            if sum ==1:
                return True
            if sum in seen:
                return False
            seen.add(sum)
            n=sum
