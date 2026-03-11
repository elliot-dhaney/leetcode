class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        n = len(grid)

        # Get the index of the row/col that maximizes each col/row (respectively)
        maxIndByCol = [0 for i in range(n)]
        maxIndByRow = [0 for i in range(n)]
        for rowIndex in range(n):
            for colIndex in range(n):
                if (grid[rowIndex][colIndex] > grid[rowIndex][maxIndByRow[rowIndex]]):
                    maxIndByRow[rowIndex] = colIndex
                if (grid[rowIndex][colIndex] > grid[maxIndByCol[colIndex]][colIndex]):
                    maxIndByCol[colIndex] = rowIndex

        # Accumulate in our output the difference between each cell and the 
        # minimum of the max values in its row/col.
        maxTotal = 0
        for rowInd in range(n):
            maxColIndForRow = maxIndByRow[rowInd]
            for colInd in range(n):
                maxRowIndForCol = maxIndByCol[colInd]
                maxTotal += (
                    min(grid[rowInd][maxColIndForRow], grid[maxRowIndForCol][colInd]) - 
                    grid[rowInd][colInd]
                )

        return maxTotal

    def solve(self, inputs):
        return self.maxIncreaseKeepingSkyline(inputs['grid'])
