'''
Input: head = [5,3,1,2,5,1,2]
Output: [1,3]

Problem : we need to find the minimum and maximum distance betweeen maxima and minima . 
maxima means current val is maxmim then  previous and forward node val and simliar to minima vice vase.

in the above example node 1 , 5, 1 are the maximum and minima number and their positions are 2,4,5
so maximum distace is 5-2 = 3 
and minima distace will be = 1 because minmum distace between 5-4 is 1 so we return the [1,3] as output
'''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        if not head or not head.next or not head.next.next:
            return [-1,-1]
        prev = head
        current = head.next
        position = 1
        points = []
        while current.next :
            if (current.val > prev.val and current.val > current.next.val) or ( current.val < prev.val and current.val < current.next.val):
                points.append(position)
            prev = current
            current = current.next
            position +=1
        print(points)
        if len(points) < 2:
            return [-1,-1]
            
        min_dis = float('inf')
        max_dis = points[-1] - points[0]
        for i in range(1,len(points)):
            min_dis = min(min_dis,points[i]-points[i-1])
        return [min_dis , max_dis]


def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Example usage:
solution = Solution()
head = [5, 3, 1, 2, 5, 1, 2]
linked_list_head = create_linked_list(head)
ans = solution.nodesBetweenCriticalPoints(linked_list_head)
print(ans)  # Output the result
