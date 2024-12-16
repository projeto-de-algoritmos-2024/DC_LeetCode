from typing import List
import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Helper function to merge two skylines
        def mergeSkylines(left, right):
            h1, h2 = 0, 0
            i, j = 0, 0
            merged = []
            while i < len(left) and j < len(right):
                if left[i][0] < right[j][0]:
                    x, h1 = left[i]
                    i += 1
                elif left[i][0] > right[j][0]:
                    x, h2 = right[j]
                    j += 1
                else:
                    x, h1 = left[i]
                    h2 = right[j][1]
                    i += 1
                    j += 1
                maxH = max(h1, h2)
                if not merged or merged[-1][1] != maxH:
                    merged.append([x, maxH])
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        # Base case
        if not buildings:
            return []
        if len(buildings) == 1:
            left, right, height = buildings[0]
            return [[left, height], [right, 0]]

        # Divide
        mid = len(buildings) // 2
        leftSkyline = self.getSkyline(buildings[:mid])
        rightSkyline = self.getSkyline(buildings[mid:])

        # Conquer
        return mergeSkylines(leftSkyline, rightSkyline)
