class Solution:
    def findLonely(self, nums):
        seen = set()
        lonelyNums = set()
        for num in nums:
            wasSeen = False
            if (num in seen):
                lonelyNums.discard(num)
                wasSeen = True
            if (num-1 in seen):
                lonelyNums.discard(num-1)
                wasSeen = True
            if (num+1 in seen):
                lonelyNums.discard(num+1)
                wasSeen = True
            if (not wasSeen):
                lonelyNums.add(num)

            seen.add(num)

        return list(lonelyNums)

    def solve(self, inputs):
        return self.findLonely(inputs['nums'])
