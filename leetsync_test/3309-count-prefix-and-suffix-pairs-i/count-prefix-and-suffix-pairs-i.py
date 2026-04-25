class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if (self.isPrefixAndSuffix(words[i], words[j])):
                    count += 1

        return count


    def isPrefixAndSuffix(self, str1, str2):
        return str2.startswith(str1) and str2.endswith(str1)