# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Hash Map Approach
class Solution:
    def hasCycle(self, head) -> bool:
        visited = set()
        current = head
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
        return False

# Two Pointers Approach -> Floyd's Cycle Detection

    def hasCycle_pointers(self, head) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False



