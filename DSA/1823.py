'''
it is related to Josephus problem - 
Given 𝑛  people standing in a circle, every k-th person is eliminated until only one person remains. 
The task is to find the position of this last remaining person.

step 1 = we created a list naming friends , index as 0 
step 2 = next we need to iterate using while loop untill our size if the array becomes 1
we applying one formula for claculating the index at each time by using 
index = (index + k - 1) % len(friends) after finding the index at each iteration we have to remove that element from the 
friends list 
step 3 : when the friends array becomes 1 then the loop will exits and we return the frist element from friends list

'''
class Solution:
    def findTheWinner(self, n, k):
        friends = list(range(1, n + 1))  # Create a list of friends numbered from 1 to n
        index = 0  # Start at the 1st friend (index 0 in the list)
        while len(friends) > 1:
            # Find the next friend to be removed
            index = (index + k - 1) % len(friends)
            # Remove that friend from the circle
            friends.pop(index)
        
        # The last remaining friend is the winner
        return friends[0]

# Example usage:
solution = Solution()
print(solution.findTheWinner(5, 2))  # Output: 3
