'''
Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.

we neee to find the number of bottle we can drink and also we can make exchange the empty bottle to get filled water bottle , 
so initially drink the available numBottle , so res = numBottles ,
next , we need to find the cur_empty by divind the cur_empty // numExchange so at frist iteration it will give 3 and next left_empty will become 0 then res = 12 and cur_empty is 0+3
next we need to see that cur_empty is greater then then numExhange so we iterting the loop so now full_drink becomes = 3//3 so it will be 1 . and leftempty is 0 and res = 12 
cur_empty will become 1 
so next iteration condition becomes false so we will exit the loop and return the ans 13. 
'''
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        res = numBottles
        cur_empty = numBottles
        while cur_empty >= numExchange:
            full_drinked = cur_empty // numExchange
            left_empty = cur_empty % numExchange
            res += full_drinked
            cur_empty = left_empty + full_drinked
        return res
