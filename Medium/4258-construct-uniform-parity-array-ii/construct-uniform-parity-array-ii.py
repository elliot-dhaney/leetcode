class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # If min(nums1) is odd - all lists return True
        # If min(nums1) is even - all numbers must be even

        minNum = 10 ** 10
        hasOdd = False
        for num in nums1:
            if (num < minNum):
                minNum = num
            if (num % 2 == 1):
                hasOdd = True

        if (minNum % 2 == 0 and hasOdd):
            return False
        return True
