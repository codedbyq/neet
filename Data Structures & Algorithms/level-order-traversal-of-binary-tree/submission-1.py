# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        result = []                             # [[1],[2,3],[4,5,6,7]]

        if root:
            queue.append(root)
        
        while queue:                            # []
            vals_in_level = []                  # [4,5,6,7]
            for _ in range(len(queue)):         # 4 < 4
                curr = queue.popleft()
                vals_in_level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(vals_in_level)

        return result