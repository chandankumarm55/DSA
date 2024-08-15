class Solution(object):
    def myPow(self, x, n):
        if n==0:
            return 1 
        if n<0:
            x=1/x
            n=-n
        ans =1
        current=x
        while n > 0:
            if n%2 ==1 :
                ans*=current
            current*=current
            n=n//2
            print(n,ans,current)
        return ans
