class Solution:
    def maxCompatibilitySum(self, students, mentors):
        self.memo = {}

        # First, compute full 2D array scores[i][j] = compScore(student[i], mentor[j]) (O(m^2 * n))
        self.scores = []
        for i in range(len(students)):
            row = []
            for j in range(len(mentors)):
                row.append(self.calculateCompatibilityScore(students[i], mentors[j]))
            self.scores.append(row)

        # Problem is now find max sum in scores taking exactly 1 element from each
        # row and column. # The search space is O(m!), can address that by going
        # row-by-row and memoizing the max for each selection of j1,j2,j3,... that
        # rows 1,2,3... have used. More precisely:

        # If s is a m-bit binary string, and k is the highest nonzero bit of s, 
        # then memo[s] stores the max compatability sum for scores[k+1:] where
        # s[l] == 1 only for columns l that have not been picked yet.
        # There are 2^m such values in memo. With m<=8 this is very reasonable.
        availableCols = [i for i in range(len(students))]
        maxValue = self.computeMaxCompatibilitySum(0, availableCols)
        return maxValue

    def computeMaxCompatibilitySum(self, currentRow, availableCols):
        # Check our memoization
        memoKey = self.getMemoKey(availableCols)
        if (memoKey in self.memo):
            return self.memo[memoKey]

        # Base cases
        if (currentRow == len(self.scores)):
            return 0

        maxValue = -1
        for colIndex in range(len(availableCols)):
            col = availableCols[colIndex]
            nextCols = availableCols[:colIndex] + availableCols[colIndex+1:]              

            # Get the max sum of the remaining rows/cols if we use this row,col pair.
            maxSubSum = self.computeMaxCompatibilitySum(
                currentRow + 1,
                nextCols
            )

            maxValue = max(maxValue, maxSubSum + self.scores[currentRow][col])

        self.memo[memoKey] = maxValue
        return maxValue
        
    def getMemoKey(self, availableCols):
        binNum = 0
        for col in availableCols:
            binNum += 2 ** col
        return binNum

    def calculateCompatibilityScore(self, studentAnswers, mentorAnswers):
        score = 0
        # Problem constraints guarantees the lists are the same length.
        for answerIndex in range(len(studentAnswers)):
            if (studentAnswers[answerIndex] == mentorAnswers[answerIndex]): 
                score += 1
        return score

    def solve(self, inputs):
        return self.maxCompatibilitySum(inputs['students'], inputs['mentors'])
