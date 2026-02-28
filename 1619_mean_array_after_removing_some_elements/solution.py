class Solution:
    def trimMean(self, arr):
        arr.sort()
        perc5 = len(arr) // 20
        
        return sum(arr[perc5 : 19*perc5]) / (18 * perc5)

    def solve(self, inputs):
        return self.trimMean(inputs['arr'])
