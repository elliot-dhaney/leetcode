class Solution:
    def wordBreak(self, s, wordDict):
        # change dictionary into set
        # check substrings from largest dictionary word to smallest
        # keep set of unfinishable strings
        self.unfinishable = set()
        self.wordDict = set(wordDict)
        self.largestWordSize = 20
        
        return self.checkString(s)

    def checkString(self, s):
        if ((s in self.unfinishable) or (s == '')):
            return False

        for i in range(min(len(s), self.largestWordSize), 0, -1):
            if s[:i] in self.wordDict:
                if (i == len(s)):
                    return True
                if (self.checkString(s[i:])):
                    return True

        self.unfinishable.add(s)
        return False

    def solve(self, inputs):
        return self.wordBreak(inputs['s'], inputs['wordDict'])
