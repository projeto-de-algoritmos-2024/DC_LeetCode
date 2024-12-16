from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        # Initialize the heap with the head of each list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        dummy = ListNode()
        current = dummy

        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            current.next = ListNode(val)
            current = current.next
            node = node.next
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        return dummy.next
