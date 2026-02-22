class Solution:
    def reverseBits(self, n):
        digitMask = 1
        reverse = 0

        # Notably, the constraints mention that n is signed but not negative.
        # It is also even. So the first and last bits are both 0.
        for i in range(31):
            n >>= 1
            digit = digitMask & n
            if (reverse > 0 or digit == 1):
                reverse <<= 1
                reverse |= digit

        return reverse
    def solve(self, inputs):
        return self.reverseBits(inputs['n'])
