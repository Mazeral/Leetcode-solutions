# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        linked_vals = []
        current = head
        while current is not None:
            linked_vals.append(current.val)
            current = current.next
        result = linked_vals[0] + linked_vals[-1]
        l: int = len(linked_vals) // 2
        for i in range(1, l):
            twin_index = len(linked_vals) - 1 - i
            twin_sum = linked_vals[i] + linked_vals[twin_index]
            result = max(result, twin_sum)
        return result
