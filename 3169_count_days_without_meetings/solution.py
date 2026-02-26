class Solution:
    def countDays(self, days, meetings):
        numDays = days

        meetings.sort()
        lastDay = -1
        for meeting in meetings:
            if (meeting[1] < lastDay):
                continue
            elif (meeting[0] <= lastDay):
                numDays -= (meeting[1] - lastDay)
            else:
                numDays -= (meeting[1] - meeting[0] + 1)
            lastDay = meeting[1]

        return numDays
        
    def solve(self, inputs):
        return self.countDays(inputs['days'], inputs['meetings'])
