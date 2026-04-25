class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        currentPt = points[0]
        numSteps = 0
        for i in range(1, len(points)):
            nextPt = points[i]
            xDiff = abs(currentPt[0] - nextPt[0])
            yDiff = abs(currentPt[1] - nextPt[1])

            # First, find how many diagonal steps are possible
            diagSteps = min(xDiff, yDiff)

            # Then, take the remaining horizontal and vertical steps (separately) 
            # and remove the diagonal steps.
            numSteps += (xDiff + yDiff - min(xDiff, yDiff))

            currentPt = nextPt

        return numSteps