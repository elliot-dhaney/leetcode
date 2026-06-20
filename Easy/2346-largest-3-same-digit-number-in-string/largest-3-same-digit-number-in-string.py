class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            checkVal = f'{i}{i}{i}'
            if (num.find(checkVal) != -1):
                return checkVal
        return ""
