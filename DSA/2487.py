class Solution(object):
    def removeNodes(self, head):
        # Check if the head is None or if there's only one node in the list
        if not head or not head.next:
            return head
        
        # Create a stack to keep track of nodes with greater values
        stack = []
        current = head
        
        # Traverse the linked list
        while current:
            # Check if the stack is not empty and the current node's value is greater
            while stack and stack[-1].val < current.val:
                stack.pop()
            
            # Add the current node to the stack
            stack.append(current)
            current = current.next
        
        # Update the next pointers of nodes in the stack
        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]
        
        # Set the next pointer of the last node in the stack to None
        stack[-1].next = None
        
        # Return the head of the modified linked list
        return stack[0]
