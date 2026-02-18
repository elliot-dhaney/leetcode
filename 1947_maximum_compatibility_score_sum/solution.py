class Solution:
    def maxCompatibilitySum(self, students, mentors):
        return 0

    def calculateCompatibilityScore(self, studentAnswers, mentorAnswers):
        score = 0
        # Problem constraints guarantees the lists are the same length.
        for answerIndex in range(len(studentAnswers)):
            if (studentAnswers[answerIndex] == mentorAnswers[answerIndex]): 
                score += 1
        return score

    def solve(self, inputs):
        return self.maxCompatibilitySum(inputs['students'], inputs['mentors'])
