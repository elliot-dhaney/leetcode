class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        # incrementally sum. Every time the sum is 0, it returns.
        incrSum = 0
        boundaryCount = 0
        for num in nums:
            incrSum += num
            if (incrSum == 0):
                boundaryCount += 1
        return boundaryCount