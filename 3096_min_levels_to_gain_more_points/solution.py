class Solution:
    def minimumLevels(self, possible):
        # Total available points is constant, so just play games until we reach 
        # a winning state.
        numGames = len(possible)

        leftScore = 2 * possible[0] - 1
        rightScore = (2 * sum(possible) - numGames) - leftScore # total score - first game

        index = 1
        while (leftScore <= rightScore and index < numGames - 1):
            scoreFromGame = 2 * possible[index] - 1
            leftScore += scoreFromGame
            rightScore -= scoreFromGame
            index += 1
        
        if (leftScore > rightScore):
            return index
        return -1

    def solve(self, inputs):
        return self.minimumLevels(inputs['possible'])
