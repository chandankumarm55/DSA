'''
 
Example 1:

Input: n = 4, time = 5
Output: 2
Explanation: People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2.
After five seconds, the 2nd person is holding the pillow.
Example 2:

Input: n = 3, time = 2
Output: 3
Explanation: People pass the pillow in the following way: 1 -> 2 -> 3.
After two seconds, the 3rd person is holding the pillow.

Solution :
we can solve this problem by tracking the direction and we can update the position by direction 

we initially have position is 1 because when we pass the frist pass it will cross two nodes and also direction is 1 because
we should initially move from left to right in this direction we plus the direction so we update the position .

in the same time if the position equal to n that means we are in last element of the number so now we need to come back now 
so we change the direction and we are decreament the now and if the time over for loop exits and we return the current position
'''
class Solution(object):
    def passThePillow(self, n, time):
        position = 1
        direction = 1
        for _ in range(time):
            position+=direction
            if position ==1:
                direction =1
            elif position ==n :
                direction =-1
        return position

