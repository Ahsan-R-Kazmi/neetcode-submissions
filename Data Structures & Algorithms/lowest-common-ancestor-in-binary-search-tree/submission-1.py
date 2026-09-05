# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        ans = None

        def dfs(node: TreeNode):
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
                return True

            return left or right

        dfs(root)
        return ans
