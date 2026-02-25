import copy

class Solution:
    def combinationSum2(self, candidates, target):
        self.memo = dict()
        candidates.sort()
        self.candidates = candidates

        output = self.check(0, target)
        self.removeDuplicateCombis(output)

        return output

    def check(self, index, target):
        if (index >= len(self.candidates)):
            return []

        candidate = self.candidates[index]
        if (candidate > target):
            # Return early since the list is sorted.
            return []

        memoKey = str(index) + ',' + str(target)
        if (memoKey in self.memo):
            return copy.deepcopy(self.memo[memoKey])
            
        if (candidate == target):
            self.memo[memoKey] = copy.deepcopy([[candidate]])
            return [[candidate]]

        withCandidate = self.check(index + 1, target - candidate)
        self.removeDuplicateCombis(withCandidate)
        for candidateSum in withCandidate:
            candidateSum.append(candidate)

        noCandidate = self.check(index + 1, target)
        self.removeDuplicateCombis(noCandidate)
        output = withCandidate + noCandidate

        self.memo[memoKey] = copy.deepcopy(output)
        return output
 
    def removeDuplicateCombis(self, combis):
        seen = set()
        indicesToRemove = []
        for index in range(len(combis)):
            subStr = str(combis[index])
            if (subStr in seen):
                indicesToRemove.append(index)
            seen.add(subStr)

        i = 0
        for index in indicesToRemove:
            combis.pop(index - i)
            i += 1        

    def solve(self, inputs):
        return self.combinationSum2(inputs['candidates'], inputs['target'])
