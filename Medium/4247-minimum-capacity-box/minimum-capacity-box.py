class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        minInd = -1
        minCap = 1000
        for ind, cap in enumerate(capacity):
            if (cap >= itemSize and cap < minCap):
                minCap = cap
                minInd = ind
        return minInd
