class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result = result ^ num

        return result

# if nums[0] is 0 at a bit, it has no effect on the xor.
# if nums[0] is 1 at a bit when i=0, its also 1 when j=0 so it has no effect
# if nums[0] is 1 at a bit when k=0, it only affects for pairs (i,j) where they are not both 0. 

# So: 
# 1) Count the number of non-zero bits for each bit digit. (call that a)
# 2) Then determine the number of non-zero pairs. (simple product a * a)
# 3) xor that value as many times as there are nonzero bits in that location. (a times)

# Which means for each bit the result is a^3 % 2. This is 1 iff a is odd
# Or. In other words. This is 1 iff the xor of all the bits at that digit is 1.
# Or. In other words. The result is simply the xor of all the numbers in the array
