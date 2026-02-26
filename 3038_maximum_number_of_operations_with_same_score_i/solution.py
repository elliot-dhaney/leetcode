class Solution:
    def maxOperations(self, nums):
        i = 0
        count = 0
        while (i <= len(nums) - 2):
            newSum = nums[i] + nums[i+1]
            if (i >= 2):
                firstSum = nums[0] + nums[1]
                if (newSum == firstSum):
                    count += 1
                else:
                    break
            else:
                count += 1
            i += 2
        return count

    def solve(self, inputs):
        return self.maxOperations(inputs['nums'])
