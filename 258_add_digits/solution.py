class Solution:
    def addDigits(self, num):
        return self.addDigitsSmart(num)

    def addDigitsSmart(self, num):
        if (num == 0): 
            return 0
        if (num % 9 == 0):
           return 9
        return num % 9

    def addDigitsNaive(self, num):
        # Continue until we are left with only 1 digit.
        while (num >= 10):

            # Add digits of num together.
            newNum = 0
            while (num >= 1):
                newNum += num % 10
                num //= 10

            # Replace num with the sum of its digits.
            num = newNum

        return num

    def solve(self, inputs):
        return self.addDigits(inputs['num'])
