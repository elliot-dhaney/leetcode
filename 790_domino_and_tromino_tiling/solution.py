class Solution:
    def numTilings(self):
    memo = {1: 1, 2: 2, 3: 5, 4: 11}
    MOD = (10 ** 9) + 7

    def numTilings(self, n: int) -> int:
        if (n in self.memo):
            return self.memo[n]

        total = (2 * self.numTilings(n-1) + self.numTilings(n-3)) % self.MOD
        self.memo[n] = total
        return total

    def solve(self, inputs):
        return self.numTilings(inputs['n'])


# k-1 = 2*1 + 2*2 + 2*3 + ... + 2* (k-4) + (k-3) + (k-2) + 2
# 2 * (k-1) = (k-1) + (2 + (k-2) + (k-3) + 2 * (k-4) ... +2*2 + 2*1)
#   =>
# k = 2 * (k-1) + (k-3)
