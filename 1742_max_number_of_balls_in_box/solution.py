class Solution:
    def countBalls(self, lowLimit, highLimit):
        counts = dict()
        maxCount = 1

        # Count digitSums, and keep track of the max count.
        for ball in range(lowLimit, highLimit + 1):
            digitSum = self.sumDigits(ball)
            if (digitSum in counts):
                counts[digitSum] += 1
                if (counts[digitSum] > maxCount):
                    maxCount = counts[digitSum]
            else:
                counts[digitSum] = 1

        return maxCount

    def sumDigits(self, digits):
        digitSum = 0
        while (digits > 0):
            digitSum += (digits % 10)
            digits = digits // 10
        return digitSum

    def solve(self, inputs):
        return self.countBalls(inputs['lowLimit'], inputs['highLimit'])
