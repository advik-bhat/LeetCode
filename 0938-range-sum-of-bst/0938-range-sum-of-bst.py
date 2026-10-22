# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, node: TreeNode | None, low: int, high: int) -> int:
        if node is None:
            return 0
        elif node.val > high:
            return self.rangeSumBST(node.left, low, high)
        elif node.val < low:
            return self.rangeSumBST(node.right, low, high)
        else:
            total = node.val
            total += self.rangeSumBST(node.left, low, high)
            total += self.rangeSumBST(node.right, low, high)
            return total
        