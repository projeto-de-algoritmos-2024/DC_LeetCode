from typing import List, Optional
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}" if self.next else f"{self.val}"


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        # Step 1: Add the initial nodes of all lists to the heap
        for i, node in enumerate(lists):
            if node:  # Only add non-empty nodes
                heapq.heappush(min_heap, (node.val, i, node))

        # Step 2: Use a dummy node to build the merged list
        dummy = ListNode()
        current = dummy

        while min_heap:
            # Step 3: Extract the smallest node from the heap
            val, i, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next

            # Step 4: Add the next node from the same list to the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        # Step 5: Return the merged list starting at dummy.next
        return dummy.next
