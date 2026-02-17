class Solution:
    def __init__(self):
        self.ageStartIndex = 11
        self.ageEndIndex = 12

    def countSeniors(self, details):
        # Filter out any passengers who aren't strictly older than 60, then get
        # the length of that filtered list.
        return len([detail for detail in details if (
            int(detail[self.ageStartIndex: self.ageEndIndex + 1]) > 60
        )])

    def solve(self, inputs):
        return self.countSeniors(inputs['details'])
