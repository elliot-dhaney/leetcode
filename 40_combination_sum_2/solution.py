class Solution:
    def combinationSum2(self, candidates, target):
        self.memo = dict()
        candidates.sort()

        self.candidates = candidates
        self.target = target

        sums = self.findCombinations(0, target)
        self.removeDuplicateCombis(sums)

        output = self.cleanSums(sums)
        return output

    def findCombinations(self, index, target):
        if (index >= len(self.candidates)):
            return []

        candidate = self.candidates[index]
        if (candidate > target):
            # Return early since the list is sorted.
            return []

        memoKey = str(index) + ',' + str(target)
        if (memoKey in self.memo):
            return self.memo[memoKey]
            
        if (candidate == target):
            self.memo[memoKey] = [str(candidate)]
            return [str(candidate)]

        withCandidate = self.findCombinations(index + 1, target - candidate)
        noCandidate = self.findCombinations(index + 1, target)

        output = []
        for combi in noCandidate:
            output.append(combi)
        for candidateSum in withCandidate:
            output.append(candidateSum + ',' + str(candidate))

        self.memo[memoKey] = output

        return output
 
    def removeDuplicateCombis(self, combis):
        seen = set()
        indicesToRemove = []
        for index in range(len(combis)):
            subStr = combis[index]
            if (subStr in seen):
                indicesToRemove.append(index)
            seen.add(subStr)

        i = 0
        for index in indicesToRemove:
            combis.pop(index - i)
            i += 1

    def cleanSums(self, sums):
        output = []
        for sumStr in sums:
            sumLst = sumStr.split(',')
            for i in range(len(sumLst)):
                sumLst[i] = int(sumLst[i])
            output.append(sumLst)
        return output

    def solve(self, inputs):
        return self.combinationSum2(inputs['candidates'], inputs['target'])
