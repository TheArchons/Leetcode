class Solution:
    def permute(self, nums):
        def dfs(nums, curr, visited):
            if len(curr) == len(nums):
                return [curr]
            
            res = []
            for num in nums:
                if not num in visited:
                    visited.add(num)
                    res += dfs(nums, curr + [num], visited)
                    visited.remove(num)
            
            return res
        
        return dfs(nums, [], set())

sol = Solution()
print(sol.permute([1,2,3]))