# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: 
            return 

        stack = []
        length = 0 
        cur = head

        while cur: 
            stack.append(cur)
            length += 1
            cur = cur.next
        
        cur = head 

        for i in range(length // 2): 
            tail = stack.pop()

            node = cur.next
            cur.next = tail 
            tail.next = node 

            cur = node 
        
        cur.next = None