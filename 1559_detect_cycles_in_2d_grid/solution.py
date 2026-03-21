class Solution:
    def containsCycle(self, grid):
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])

        # All values will be of form row * m + col
        self.allSeen = set()
        startVal = 0
        while (len(self.allSeen) < self.m * self.n):
            # Find an unvisited chain
            for i in range(startVal, self.m * self.n):
                if (i not in self.allSeen):
                    startVal = i
                    break

            # Check if the contiguous chain contains a cycle
            row, col = self.getCoords(startVal)
            if (self.checkIsCycle(startVal, self.grid[row][col])):
                return True
        
        return False
    
    def checkIsCycle(self, startVal, startLetter):
        # Pretty traditional graph search. Just some extra code since the format
        # of the graph is a bit harder to work with.

        frontier = [[startVal, startVal]] # [ [val, fromVal]] 
        seen = {startVal}
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while (len(frontier) > 0):
            nextCell = frontier.pop()
            row, col = self.getCoords(nextCell[0])

            for offset in dirs:
                newRow, newCol = row + offset[0], col + offset[1]
                if (newRow < 0 or newCol < 0 or newRow >= self.m or newCol >= self.n):
                    continue
                if (self.grid[newRow][newCol] != self.grid[row][col]):
                    continue

                newVal = self.n * newRow + newCol
                if (newVal == nextCell[1]):
                    continue

                if (newVal in seen):
                    return True

                seen.add(newVal)
                frontier.append([newVal, nextCell[0]])        

        self.allSeen.update(seen)
        return False
    
    def getCoords(self, val):
        return val // self.n, val % self.n

    def solve(self, inputs):
        return self.containsCycle(inputs['grid'])
