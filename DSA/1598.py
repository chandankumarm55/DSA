'''
Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2
Explanation: Use this change folder operation "../" 2 times and go back to the main folder.

step 1 : Initialize the distance variable to 0 

step 2 : The code iterates through each entry in the logs list. For each entry, it checks if the entry is ../, ./, 
or any other folder name.
If the entry is ../, it means moving up one directory level. If distance is greater than 0, decrement distance by 1.
If the entry is ./, it means staying in the current directory, so no change is made.
For any other folder name, it means moving into a new directory, so distance is incremented by 1.

step 3 : return the distance if it is greater then 0 other wise return 0

'''

class Solution(object):  
    def minOperations(self, logs):
        distance = 0
        for char in logs:
            if char == '../':
                if distance >0:
                    distance-=1
            elif char == './':
                continue
            else :
                distance+=1
        if distance >=0 :
            return distance
        else :
            return 0
        
