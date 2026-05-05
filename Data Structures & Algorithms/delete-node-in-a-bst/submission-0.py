# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
                        6
                4               9
            1       4     
                    2    5
"""
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            # found our key
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            # both children so we find the smallest of the right subtree to maintain bst
            curr = root.right
            while curr and curr.left:
                curr = curr.left
            
            root.val = curr.val
            root.right = self.deleteNode(root.right, root.val)

        return root