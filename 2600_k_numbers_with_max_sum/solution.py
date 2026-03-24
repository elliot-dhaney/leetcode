class Solution:
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        return (
            min(numOnes, k) -
            max(0, min(numNegOnes, k - numOnes - numZeros))
        )
        
    def solve(self, inputs):
        return self.kItemsWithMaximumSum(
            inputs['numOnes'], 
            inputs['numZeros'], 
            inputs['numNegOnes'], 
            inputs['k']
        )
