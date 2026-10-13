# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        return self.countSubDominantNodes(root)[0]
    
    def countSubDominantNodes(self, root):
        leftMax = -1
        rightMax = -1
        leftCount = 0
        rightCount = 0
        if (root.left != None):
            [leftCount, leftMax] = self.countSubDominantNodes(root.left)
        if (root.right != None):
            [rightCount, rightMax] = self.countSubDominantNodes(root.right)

        count = leftCount + rightCount
        if (root.val >= max(leftMax, rightMax)):
            return [count + 1, root.val]
        else:
            return [count, max(leftMax, rightMax)]