'''
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
 we can easily solve this problem by using simple steps
 1:create a result list and find the length of the intervals
 2:iterstive over intervals and stop when the constion of  i<n and intervals[i][1]<newInterval[0] breaks 
 it means we enter the interval which should be merge with new interval
 3:next iterative over the  intervals and try to find the merged new interval by using below condition
  while i< n and intervals[i][0]<=newInterval[1]:
            newInterval[0]=min(newInterval[0],intervals[i][0])
            newInterval[1]=max(newInterval[1],intervals[i][1])
            i+=1
and append the newIntervals to result 
4:last step is to iterate the itervals and addd the remaining interval items into result
'''
class Solution:
    def insert(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)
        
        while i<n and intervals[i][1]<newInterval[0]:
            result.append(intervals[i])
            i+=1
        while i< n and intervals[i][0]<=newInterval[1]:
            newInterval[0]=min(newInterval[0],intervals[i][0])
            newInterval[1]=max(newInterval[1],intervals[i][1])
            i+=1
        result.append(newInterval)
        while i<n:
            result.append(intervals[i])
            i+=1
        return result

