# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], nodes: List[int]) -> None:
        if not root:
            return None

        self.dfs(root.left, nodes)
        nodes.append(root.val)
        self.dfs(root.right, nodes)
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        self.dfs(root, result)
        return result