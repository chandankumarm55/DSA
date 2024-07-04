'''
The problem = You are given the head of a linked list, which contains a series of integers separated by 0's. 
The beginning and end of the linked list will have Node.val == 0.
For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is 
the sum of all the merged nodes. The modified list should not contain any 0's.

Sample Output = 
Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.

step1 : Create new dummy linked list so we can store the new linked list of sum of numbers between zeros
so , we need know that frist element is 0 so we can iterate from 1 element of the list so it will dont by following code :
dummy = ListNode()
        current = dummy
        root=head.next
        total = 0

step 2 : we need to check the val of the current node that is root.val if it not equal to 0 then we need to add that value to the 
total so we can add futher in new list 
code : 
if root.val !=0:
                total+=root.val

step 3 : if the given root.val is equal to 0 that means we need to add the total val to the new head so we need to create new
node wiith that total element and also we need point the current element to current.next to point the next element and make total =0

code : if total !=0:
                    current.next= ListNode(total)
                    current = current.next
                total = 0
step 4 : at the end of the current while loop so we need to point the root element to next of the root node 
then the final output of dummy will be 
dummy = [0 , 4 , 11 ] 
so we need retuen the dummy.next element 
 then the ans will be [4 , 11 ]

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        dummy = ListNode()
        current = dummy
        root=head.next
        total = 0
        while root is not None:
            if root.val !=0:
                total+=root.val
            else:
                if total !=0:
                    current.next= ListNode(total)
                    current = current.next
                total = 0
            root = root.next
        return dummy.next
        
