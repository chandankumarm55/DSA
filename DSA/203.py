#Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

class Solution(object):
    def removeElements(self, head, val):
        # Create a dummy node to simplify operations
        dummy=ListNode(0)
        dummy.next=head
        current=dummy
        while  current .next:
            if current.next.val == val:
                current.next=current.next.next
            else:
                current=current.next
        return dummy.next
