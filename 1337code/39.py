class Solution:
    def combinationSum(self, candidates, target: int):
        def dfs(curr, target, sum, candidates):
            if sum > target:
                return None
            if sum == target:
                return [curr]
            
            res = []
            
            for cand in candidates:
                if (not curr or cand <= curr[-1]) and sum + cand <= target:
                    resOne = dfs(curr + [cand], target, sum + cand, candidates)
                    if resOne:
                        res += resOne
            
            return res

        return dfs([], target, 0, candidates)

sol = Solution()
print(sol.combinationSum([2,3,6,7], 7))