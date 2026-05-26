class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # OR is a strictly nondecreasing function wrt the quantity of inputs.
        # So the max is just the OR of the whole list. 
        self.n = len(nums)
        self.nums = nums

        self.maxOR = 0
        for num in nums:
            self.maxOR = self.maxOR | num
        
        return self.calculateQuantity(0, 0)

    def calculateQuantity(self, currentOR, index):
        if (currentOR >= self.maxOR):
            return 2 ** (self.n - index)
        if (index >= self.n):
            return 0


        quantity = 0
        
        # Don't include the current element
        quantity += self.calculateQuantity(currentOR, index+1)
        
        # Include the current element
        quantity += self.calculateQuantity(currentOR | self.nums[index], index+1)
        
        return quantity
