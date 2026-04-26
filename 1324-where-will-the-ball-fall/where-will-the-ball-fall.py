class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        self.grid = grid 
        self.m = len(grid)
        self.n = len(grid[0])
        ballPositions = [ i for i in range(self.n) ]

        row = 0
        while (row < self.m):
            # Returns True if all of the balls are stuck.
            if (self.playRow(ballPositions, row)):
                return ballPositions

            row += 1
        
        return ballPositions

    def playRow(self, ballPositions, row):
        allStuck = True
        for index, ballCol in enumerate(ballPositions):
            if (ballCol == -1):
                continue

            # Get the column after the cell redirects the ball.
            shiftedBall = ballCol + self.grid[row][ballCol]
            if (0 <= shiftedBall < self.n):
                # Check if neighboring cell forms a wedge.
                if (self.grid[row][shiftedBall] == self.grid[row][ballCol] * -1):
                    ballPositions[index] = -1
                else:
                    ballPositions[index] = shiftedBall 
                    allStuck = False
            else:
                ballPositions[index] = -1

        return allStuck

            
