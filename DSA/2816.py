'''
orginal linked list -189
Frist step ius to reverse the current linked list 
now the linked list will be 981
second step is tp double the each number with carry 
 while current :
            dbl_value=current.next*2+carry
            current.val=dbl.val%10
            carry=dbl_value//10
            if not current.next and carry>1:
                current,next=ListNode(carry)
                break
now the list will be  8731

now reverse the linked list but leave the last carry 1 
then finnally linked list will be 378

'''


class Solution:
    def doubleIt(self, head):
        prev=None
        current=head
        while current:
            new_node=current.next
            current.next=prev
            prev=current
            current=new_node
        head=prev
        
        carry=0
        current=head
        while current :
            dbl_value=current.val*2+carry
            current.val=dbl_value%10
            carry=dbl_value//10
            if not current.next and carry>0:
                current.next=ListNode(carry)
                break
            current=current.next
        prev=None
        current=head
        while current:
            new_node = current.next
            current.next = prev
            prev=current
            current=new_node
        return prev
        
    
