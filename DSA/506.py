'''this is question easly solved by python inbuilt functions like sort , values ,
1st step : convertt the given list into decending order and store in dummy variable 
2nd step : create a  dictionary={}
3rd step : itrate over the dummy list and update the dictinary 
4th step :  convert the distinary into list by using   result=[dictionary[score[i]] for i in range(length)] this code 
'''


class Solution(object):
    def findRelativeRanks(self, score):
        length=len(score)
        dummy=sorted(score,reverse=True)
        print(dummy)
        dictionary={}
       
        for i in range(length):
            if i==0:
                dictionary[dummy[i]]= 'Gold Medal'
            elif i==1:
                dictionary[dummy[i]]='Silver Medal'
            elif i==2:
                dictionary[dummy[i]]='Bronze Medal'
            else:
                dictionary[dummy[i]]=str(i+1)
        result=[dictionary[score[i]] for i in range(length)]
    
        
        return result

solution=Solution()
score = [10,3,8,9,4]
ans=solution.findRelativeRanks(score)
print(ans)
