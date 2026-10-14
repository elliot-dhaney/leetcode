class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        if (len(nums) == 1): return 1
        if (len(nums) == 2): return 0

        partialSums = self.getPartialSums(nums)

        fairCount = 0
        # Now we try removing each index.
        for i in range(len(nums)):
            [evenCount, oddCount] = self.getRemovedSums(nums, partialSums, i)
            if (evenCount == oddCount):
                fairCount += 1
        return fairCount
    
    def getRemovedSums(self, nums: list[int], partialSums: list[int], removedIndex: int) -> list[int]:
        '''
        Returns new [evenSum, oddSum] after removing removedIndex
        '''
        oddSum = partialSums[-1] if len(partialSums) % 2 == 0 else partialSums[-2]
        evenSum = partialSums[-1] if len(partialSums) % 2 == 1 else partialSums[-2]

        if (removedIndex == 0):
            return [oddSum, evenSum - nums[0]]

        # Get the even/odd partial sums of nums[removedIndex+1:], then swap parities
        # and add to the even/odd partial sums of nums[:removedIndex].
        if (removedIndex % 2 == 0):
            newEvenRH = oddSum - partialSums[removedIndex - 1]
            newOddRH = evenSum - partialSums[removedIndex]
            return [
                partialSums[removedIndex] - nums[removedIndex] + newEvenRH,
                partialSums[removedIndex - 1] + newOddRH, 
            ]
        else:
            newEvenRH = oddSum - partialSums[removedIndex]
            newOddRH = evenSum - partialSums[removedIndex - 1]
            return [
                partialSums[removedIndex - 1] + newEvenRH,
                partialSums[removedIndex] - nums[removedIndex] + newOddRH
            ]




    def getPartialSums(self, nums: list[int]) -> list[int]:
        '''
        Returns a list where index i contains the sum of elements at:
            (even i) indices 0, 2, ..., i
            (odd i) indices 1, 3, ... i
        '''
        partialSums = [0] * len(nums)
        for i in range(len(nums)):
            n = nums[i]
            partialSums[i] += n

            # Setup the next part of the partial sum.
            if (i < len(nums) - 2):
                partialSums[i+2] = partialSums[i]
        return partialSums


# 1,2,3,4,5,6,7,8
# 1,2,4,6,9,12,16,20

# remove 3 -> 
# 1,2,4,5,6,7,8
# 1,2,5,7,11,13,19