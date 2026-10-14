class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        n = len(nums)
        if (n == 1): return 1
        if (n == 2): return 0

        partialSums = self.getPartialSums(n, nums)

        # Force partialSums to be even length, for cleaner code.
        if (n % 2 == 1):
            partialSums.append(partialSums[-2])

        fairCount = 0
        # Now we try removing each index.
        for i in range(n):
            if (self.isRemovalFair(n, nums, partialSums, i)):
                fairCount += 1
        return fairCount
    
    def isRemovalFair(
        self, 
        n: int, 
        nums: list[int], 
        partialSums: list[int], 
        removedIndex: int
    ) -> bool:
        '''
        Returns True if new [evenSum, oddSum] after removing removedIndex are fair, and False otherwise
        '''

        # oddSum is forced to partialSums[-1] because we forced partialSums to be
        # even lengthed.
        if (removedIndex == 0):
            return partialSums[-1] == partialSums[-2] - nums[0]

        # Get the even/odd partial sums of nums[:removedIndex].
        if (removedIndex % 2 == 0):
            evenLH = partialSums[removedIndex] - nums[removedIndex]
            oddLH = partialSums[removedIndex - 1]
        else:
            evenLH = partialSums[removedIndex - 1]
            oddLH = partialSums[removedIndex] - nums[removedIndex]
        
        # Get the even/odd partial sums of nums[removedIndex+1:].
        oldOddRH = partialSums[-1] - partialSums[removedIndex - ((removedIndex + 1) % 2)]
        oldEvenRH = partialSums[-2] - partialSums[removedIndex - (removedIndex % 2)]

        # Add the opposite-parity LH/RH partial sums and compare.
        return (evenLH + oldOddRH == oddLH + oldEvenRH)

    def getPartialSums(self, n: int, nums: list[int]) -> list[int]:
        '''
        Returns a list where index i contains the sum of elements at:
            (even i) indices 0, 2, ..., i
            (odd i) indices 1, 3, ... i
        '''
        partialSums = [0] * n
        for i in range(n):
            if (i < 2):
                partialSums[i] = nums[i]
            else:
                partialSums[i] = partialSums[i-2] + nums[i]

        return partialSums


# 1,2,3,4,5,6,7,8
# 1,2,4,6,9,12,16,20

# remove 3 -> 
# 1,2,4,5,6,7,8
# 1,2,5,7,11,13,19