# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthLargestPerfectSubtree(self, root, k):
        # Recursively find all perfect subtree sizes, sort them in non-increasing order, 
        # then take the kth element (if it exists)
        subtreeSizes, _ = self.findPerfectSubtreeSizes(root)
        if (len(subtreeSizes) < k):
            return -1

        subtreeSizes.sort(reverse=True)
        return subtreeSizes[k-1]

    def findPerfectSubtreeSizes(self, node):
        '''
        Returns subtreeSizes: Array[int], isPerfectTree: bool 
        subtreeSizes contains the size of all perfect subtrees of node.
        '''
        if (node.left == None and node.right == None):
            return [1], True

        leftSubtrees, isPerfectLeft = [], False
        rightSubtrees, isPerfectRight = [], False
        if (node.left != None):
            leftSubtrees, isPerfectLeft = self.findPerfectSubtreeSizes(node.left)
        if (node.right != None):
            rightSubtrees, isPerfectRight = self.findPerfectSubtreeSizes(node.right)
        
        combinedSubtrees = leftSubtrees + rightSubtrees

        # If both subtrees are perfect, the whole thing is.
        perfectSubtreeSize = []
        if (isPerfectLeft and isPerfectRight and leftSubtrees[0] == rightSubtrees[0]):
            treeSize = len(combinedSubtrees) + 1
            return [treeSize] + combinedSubtrees, True

        return combinedSubtrees, False

    def solve(self, inputs):
        return self.kthLargestPerfectSubtree(inputs['root'], inputs['k'])
