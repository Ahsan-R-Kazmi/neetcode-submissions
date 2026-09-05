# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans = None

        def dfs(node: 'TreeNode'):
            nonlocal ans
            if node is None:
                return False

            left = dfs(node.left)
            right = dfs(node.right)

            if node == p or node == q:
                if left or right:
                    ans = node
                return True
            
            if ans is None and left and right:
                ans = node

            return left or right
            
        dfs(root)
        return ans

