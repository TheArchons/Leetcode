class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def dfs(self, root):
        ld = lp = rp = rd = 0
        if root.left:
            lp, ld = self.dfs(root.left)
        
        if root.right:
            rp, rd = self.dfs(root.right)
        
        mp = max(lp, rp, ld + rd)
        return (mp, max(ld, rd) + 1)

    def diameterOfBinaryTree(self, root):
        return self.dfs(root)[0]

sol = Solution()
print(sol.diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))))