'''
We need to sort the positions because we can calculate distances between consecutive positions. Initially, high will be set to an upper bound value, which is (last element - first element) / (m - 1). We begin iterating with a while loop while low <= high.

At each iteration, we calculate the mid value as low + (high - low) // 2. We then call the canWeMake helper function with the position array, mid as dist, and m as the required number of balls. If it returns True, we assign ans to mid and increment low by mid + 1; otherwise, we set high = mid - 1.

Finally, we return ans as the required distance.

The canWeMake function takes three arguments. Initially, we set lastPlaced to the starting element and countBall to 1 because at least one distance is required. We iterate from 1 to the length of the array. If arr[i] minus lastPlaced is greater than dist (which is mid in this context), we increment countBall by one and update lastPlaced to arr[i].

After each iteration, we check if countBall is greater than or equal to balls. If true, we return True; otherwise, we return False.

'''

class Solution(object):
    def maxDistance(self, position, m):
        position.sort()
        low=1
        high=(position[-1]-position[0])//(m-1)
        ans=1
        while low <= high :
            mid = low + (high-low)//2
            if self.canWeMake(position,mid,m):
                ans=mid
                low=mid+1
            else :
                high=mid-1
        return ans

    def canWeMake(self,arr,dist,balls):
        countedBall=1
        lastPlaced=arr[0]
        for i in range(1,len(arr)):
            if arr[i]-lastPlaced >= dist:
                countedBall+=1
                lastPlaced=arr[i]
            if countedBall >=balls:
                return True
        return False
                    
       
        
