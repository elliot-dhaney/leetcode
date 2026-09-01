class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        # Sort the array
        # Until empty, remove first + last elements
        # Avg and add to set...floating point issues?
        # Return the size of the set.
        nums.sort()
        distinctAvgs = set()
        while (len(nums) > 0):
            avg = (nums[0] + nums[-1]) / 2
            nums = nums[1:-1]
            distinctAvgs.add(avg)
        return len(distinctAvgs)

        