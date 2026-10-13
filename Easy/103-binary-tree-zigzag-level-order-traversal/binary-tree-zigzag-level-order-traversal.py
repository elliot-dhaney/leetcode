# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if (root == None): return []
        zigDir = -1 # 1 (left-to-right) or -1 (right-to-left)

        zigZagOrder = [[root]]
        while (len(zigZagOrder[-1]) > 0):
            nextLevel = []
            currLevel = zigZagOrder[-1]

            # Prior level is in reverse order of what we need
            index = len(currLevel) - 1

            while (index >= 0):
                node = currLevel[index]
                nextLevel.extend(self.getZigZagChildrenOrder(node, zigDir))
                index -= 1

            zigZagOrder.append(nextLevel)
            zigDir *= -1

        zigZagOrderValues = []

        # zigZagOrder always ends with an empty array, so strip it.
        for i in range(len(zigZagOrder)-1):
            r = []
            for j in range(len(zigZagOrder[i])):
                r.append(zigZagOrder[i][j].val)
            zigZagOrderValues.append(r)

        return zigZagOrderValues

    def getZigZagChildrenOrder(self, node: TreeNode, zigDir: int) -> List[Node]:
        children = []
        if (node.left != None):
            children.append(node.left)
        if (node.right != None):
            if (zigDir > 0):
                children.append(node.right)
            else:
                children.insert(0, node.right)
        return children