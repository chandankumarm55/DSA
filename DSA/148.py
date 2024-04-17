# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        slow = head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        seconed_half = slow.next
        slow.next=None
        frist_sortlist = self.sortList(head)
        second_sortlist=self.sortList(seconed_half)
        return self.merge(frist_sortlist,second_sortlist)
    def merge(self,list1,list2):
        dummy=ListNode(0)
        
        current=dummy
        while list1 and list2:
            if list1.val < list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            current=current.next
        current.next=list1 if list1 else list2
        return dummy.next
