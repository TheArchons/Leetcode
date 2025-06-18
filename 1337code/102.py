# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root, res, depth):
            if root is None:
                return
            
            if (len(res) <= depth):
                res.append([])
            
            res[depth].append(root.val)

            dfs(root.left, res, depth + 1)
            dfs(root.right, res, depth + 1)

            return

        res = []
        dfs(root, res, 0)
        return res