'''
Example :
Input: bills = [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.

Time Complexity : O(n)

Solution :
so we have only 3 currency that are 5 , 10 , 20 . and we dont have any changes at the begining we have to retrun true 
if we can handle changes other wise false

step 1 : we have to initialze the dictionary with {5: 0, 10: 0} fro keeping the track of changes of 5 and 10
step 2 : nex t iterate over the bills and check the below constions to determine the changes
            if item == 5:
                currency[item]+=1
            elif item ==10:
                if currency[5]>0:
                    currency[5]-=1
                    currency[item]+=1
                else:
                    return False
            elif item ==20:
                if currency[10] >0 and currency[5]>0:
                    currency[10]-=1
                    currency[5]-=1
                elif currency[5]>=3:
                    currency[5]-=3
                else:
                    return False
        return True
step 3 : so above we are checking the if the item is 5  that means we have to add the frequency of item 5 by one .
so if the item is 10 that means we have to return 5 to the user so we need to check if the 5 changes are availble if 
the 5 ruppe availble we need to continue other wise we need to return false . so this consition will apply for the same ruppe 
20 also . in 20 ruppe we need to check the availbility of one 10 ruppe and one 5 ruppe or three 5 ruppe coins..
'''
class Solution(object):
    def lemonadeChange(self, bills):
        currency = {5: 0, 10: 0}
        for item in bills:
            if item == 5:
                currency[item]+=1
            elif item ==10:
                if currency[5]>0:
                    currency[5]-=1
                    currency[item]+=1
                else:
                    return False
            elif item ==20:
                if currency[10] >0 and currency[5]>0:
                    currency[10]-=1
                    currency[5]-=1
                elif currency[5]>=3:
                    currency[5]-=3
                else:
                    return False
        return True
                
