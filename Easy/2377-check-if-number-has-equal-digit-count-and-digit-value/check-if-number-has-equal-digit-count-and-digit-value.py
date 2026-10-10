class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            count = num.count(str(i))
            if num[i] != str(count):
                return False
        return True
