# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        output = []
        def recurse(node):
            print('recursing on node', node)
            if not node:
                return None
            if not (node.left or node.right):
                output[-1].append(node.val)
                return None
            node.left = recurse(node.left)
            node.right = recurse(node.right)
            print('returning node', node)
            return node

        while root:
            print('1', root)
            output.append([])
            root = recurse(root)
            print('2', root)
        return output
        
