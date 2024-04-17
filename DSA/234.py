class ListNode():
    def __init__(self,val):
        self.val=val
        self.next=None
class Solution(object):
    def isPalindrome(self, head):
        prev=None
        current=head
        while current:
            newNode=current.next
            current.next=prev
            prev = current
            current=newNode
        while head and prev:
            if head.val != prev.val:
                return False
            head=head.next
            prev=prev.next
        return True
        
data1=ListNode(1)
data2=ListNode(5)
data3=ListNode(1)
data1.next=data2
data2.next=data3
solution=Solution()
ans=solution.isPalindrome(data1)
print(ans)


