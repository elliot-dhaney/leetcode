class Solution:
    def digitCount(self, num: str) -> bool:
        # Since the string is max 10 characters long, brute force is effective:
        # for i in range(len(num)):
        #     count = num.count(str(i))
        #     if (num[i] != str(count)):
        #         return False
        # return True

        # A more efficient approach
        counts = dict()
        for val in num:
            if (val in counts):
                counts[val] += 1
            else:
                counts[val] = 1

        for i in range(len(num)):
            print(i, num[i])
            if (str(i) not in counts):
                if (num[i] != '0'):
                    return False
                continue
            if (str(counts[str(i)]) != num[i]):
                return False

        return True