from typing import Tuple

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def max_path(self, root: TreeNode) -> Tuple[int, int]:
        if root == None:
            return None, None
        
        lmx1, lmx2 = self.max_path(root.left)
        rmx1, rmx2 = self.max_path(root.right)
        
        sc1 = sc2 = root.val
        if lmx1 is not None and rmx1 is not None:
            sc1 = max(sc1, root.val, lmx1, rmx1, 
                      root.val + root.left.val,
                      root.val + root.right.val,
                      root.val + root.left.val + root.right.val,
                      root.val + lmx2 + rmx2)
        if lmx2 is not None:
            sc1 = max(sc1, root.val, lmx1, 
                      root.val + root.left.val,
                      root.val + lmx2)
            sc2 = max(sc2, root.val, root.val + lmx2)
        if rmx2 is not None:
            sc1 = max(sc1, root.val, rmx1, 
                      root.val + root.right.val,
                      root.val + rmx2)
            sc2 = max(sc2, root.val, root.val + rmx2)
        # print(root.val, (lmx1, lmx2), (rmx1, rmx2), (sc1, sc2))
        return sc1, sc2
    
    def maxPathSum(self, root: TreeNode) -> int:
        r = self.max_path(root)
        return 0 if r[0] is None else max(r[0], r[1])
        