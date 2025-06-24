# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root:
                return None
            
            rRes = dfs(root.right)
            lRes = dfs(root.left)

            if rRes:
                rMax, rMin, isRInvalid = rRes
                if rMin <= root.val:
                    return (0, 0, True)
            else:
                rMax, rMin, isRInvalid = (root.val, root.val, False)
            
            if lRes:
                lMax, lMin, isLInvalid = lRes
                if lMax >= root.val:
                    return (0, 0, True)
            else:
                lMax, lMin, isLInvalid = (root.val, root.val, False)

            if isRInvalid or isLInvalid:
                return (0, 0, True)

            return (rMax, lMin, False)
        
        _, _, isInvalid = dfs(root)
        
        return not isInvalid

sol = Solution()
# [5,1,4,null,null,3,6]
# construct treenode

# root = TreeNode(5,
#     TreeNode(1),
#     TreeNode(4,
#         TreeNode(3),
#         TreeNode(6)
#     )
# )

# [2,1,3]

# root = TreeNode(2, 
#     TreeNode(1), TreeNode(3))

# [32,26,47,19,null,null,56,null,27]
root = TreeNode(32,
    TreeNode(26,
        TreeNode(19,
            None,
            TreeNode(27)
        ),
        None
    ),
    TreeNode(47,
        None,
        TreeNode(56)
    )
)

print(sol.isValidBST(root))