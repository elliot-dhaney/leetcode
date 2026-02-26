class Solution:
    def maxOperations(self, nums):
        if (len(nums) < 2):
            return 0

        i = 2
        count = 1
        firstSum = nums[0] + nums[1]
        while (i <= len(nums) - 2):
            if (nums[i] + nums[i+1] == firstSum):
                count += 1
            else:
                break
            i += 2
        return count

    def solve(self, inputs):
        return self.maxOperations(inputs['nums'])
