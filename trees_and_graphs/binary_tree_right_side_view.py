# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        nodeq = [(root, 0)]
        
        last_node = None
        last_level = None
        vals = []
        
        while len(nodeq) > 0:
            node, level = nodeq.pop(0)
            if node.left is not None:
                nodeq.append((node.left, level + 1))
            if node.right is not None:
                nodeq.append((node.right, level + 1))
            if last_node is not None:
                if last_level != level:
                    vals.append(last_node.val)
            last_node = node
            last_level = level
            
        vals.append(node.val)
            
        return vals
            
        