class Solution:
    def maximumSum(self, nums):
        optionsByMod3 = self.getNumOptions(nums)
        return self.getMaxSum(optionsByMod3)

    def getNumOptions(self, nums):
        # Retrieve the 3 biggest values in nums, for each mod 3 class.
        optionsByMod3 = { 0: [], 1: [], 2: [] }
        for num in nums:
            index = num % 3
            if (len(optionsByMod3[index]) >= 3):
                smallestVal = min(optionsByMod3[index])
                if (num > smallestVal):
                    optionsByMod3[index].remove(smallestVal)
                    optionsByMod3[index].append(num)
            else:
                optionsByMod3[index].append(num)
        return optionsByMod3

    def getMaxSum(self, optionsByMod3):
        # Either 3 of the same mod class, or 1 of each.
        sums = [0, 0, 0, 0]
        for i in range(3):
            if (len(optionsByMod3[i]) >= 3):
                sums[i] = sum(optionsByMod3[i])

        if (
            len(optionsByMod3[0]) >= 1 and 
            len(optionsByMod3[1]) >= 1 and 
            len(optionsByMod3[2]) >= 1
        ):
            sums[-1] = max(optionsByMod3[0]) + max(optionsByMod3[1]) + max(optionsByMod3[2])

        return max(sums)
    